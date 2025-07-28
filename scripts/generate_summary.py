from pathlib import Path
import json
import sys
from fpdf import FPDF


def load_data(file_path: str) -> dict:
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def build_pdf(data: dict, output_path: str) -> None:
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(0, 10, f"Daily Summary for {data.get('date')}", ln=True)
    pdf.cell(0, 10, f"Earnings: ${data.get('earnings', 0)}", ln=True)

    pdf.cell(0, 10, "Top Traffic Sources:", ln=True)
    for source, visits in data.get("traffic_sources", {}).items():
        pdf.cell(0, 10, f"- {source}: {visits}", ln=True)

    actions = data.get("actions_taken", [])
    if actions:
        pdf.cell(0, 10, "Actions Taken:", ln=True)
        for action in actions:
            pdf.cell(0, 10, f"- {action}", ln=True)

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    pdf.output(str(output_path))


def main() -> None:
    data_file = sys.argv[1] if len(sys.argv) > 1 else "sample_data.json"
    output_file = sys.argv[2] if len(sys.argv) > 2 else "output/daily_summary.pdf"
    data = load_data(data_file)
    build_pdf(data, output_file)


if __name__ == "__main__":
    main()
