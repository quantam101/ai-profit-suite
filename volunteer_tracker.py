import json
import os
from datetime import datetime
from fpdf import FPDF

DATA_FILE = "volunteers.json"
CERT_DIR = "certificates"
MILESTONES = [50, 100, 500]


def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}
    return {}


def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


def generate_certificate(name: str, milestone: int) -> str:
    os.makedirs(CERT_DIR, exist_ok=True)
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "Contributor-to-Creator Program", ln=True, align="C")
    pdf.ln(10)
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, "Certificate of Achievement", ln=True, align="C")
    pdf.ln(10)
    pdf.cell(0, 10, f"This certifies that {name}", ln=True, align="C")
    pdf.cell(0, 10, f"has completed {milestone} volunteer hours.", ln=True, align="C")
    pdf.ln(20)
    pdf.set_font("Arial", size=10)
    pdf.cell(0, 10, f"Issued on {datetime.utcnow().strftime('%Y-%m-%d')}", ln=True, align="R")
    filename = os.path.join(CERT_DIR, f"{name.replace(' ', '_')}_{milestone}_hrs.pdf")
    pdf.output(filename)
    return filename


def record_hours(name: str, hours: float) -> int:
    data = load_data()
    previous = data.get(name, 0)
    total = previous + hours
    data[name] = total
    save_data(data)

    for milestone in MILESTONES:
        if total >= milestone > previous:
            file = generate_certificate(name, milestone)
            print(f"Generated certificate for {milestone} hours: {file}")
    return total


def list_volunteers():
    data = load_data()
    for name, hours in data.items():
        print(f"{name}: {hours} hrs")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Track volunteer hours")
    parser.add_argument("name", nargs="?", help="Volunteer name")
    parser.add_argument("hours", nargs="?", type=float, help="Hours to add")
    parser.add_argument("--list", action="store_true", help="List all volunteers")

    args = parser.parse_args()

    if args.list:
        list_volunteers()
    elif args.name and args.hours is not None:
        total = record_hours(args.name, args.hours)
        print(f"{args.name} total hours: {total}")
    else:
        parser.print_help()
