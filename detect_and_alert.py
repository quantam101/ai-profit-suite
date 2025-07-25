import csv
import os
from dataclasses import dataclass
from typing import List

try:
    from twilio.rest import Client
except ImportError:
    Client = None  # Twilio not installed

@dataclass
class Product:
    name: str
    units_sold: int
    revenue: float

@dataclass
class DiscountAction:
    product: Product
    discount_percent: int

LOW_PERFORMANCE_THRESHOLD = int(os.environ.get("LOW_PERFORMANCE_THRESHOLD", 10))
DEFAULT_DISCOUNT_PERCENT = int(os.environ.get("DISCOUNT_PERCENT", 20))

def read_products(csv_path: str) -> List[Product]:
    products = []
    with open(csv_path, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            products.append(Product(
                name=row['name'],
                units_sold=int(row.get('units_sold', 0)),
                revenue=float(row.get('revenue', 0.0))
            ))
    return products


def detect_low_performers(products: List[Product]) -> List[DiscountAction]:
    low_performers = []
    for p in products:
        if p.units_sold < LOW_PERFORMANCE_THRESHOLD:
            low_performers.append(DiscountAction(product=p, discount_percent=DEFAULT_DISCOUNT_PERCENT))
    return low_performers


def send_sms(message: str) -> None:
    if Client is None:
        print("Twilio client not available. Install twilio to enable SMS.")
        return
    account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
    auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
    from_number = os.environ.get("TWILIO_FROM_NUMBER")
    to_number = os.environ.get("TO_NUMBER")
    if not all([account_sid, auth_token, from_number, to_number]):
        print("Twilio credentials not configured. Skipping SMS.")
        return
    client = Client(account_sid, auth_token)
    client.messages.create(body=message, from_=from_number, to=to_number)


def write_glide_csv(actions: List[DiscountAction], output_path: str) -> None:
    with open(output_path, 'w', newline='') as csvfile:
        fieldnames = ['name', 'units_sold', 'revenue', 'discount_percent']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for action in actions:
            writer.writerow({
                'name': action.product.name,
                'units_sold': action.product.units_sold,
                'revenue': action.product.revenue,
                'discount_percent': action.discount_percent
            })


def main(input_csv: str, output_csv: str):
    products = read_products(input_csv)
    low_performers = detect_low_performers(products)
    if not low_performers:
        print("No low-performing products found.")
        return

    # Send a summary SMS
    names = ', '.join(a.product.name for a in low_performers)
    message = f"Flash sale triggered for: {names}. Each at {DEFAULT_DISCOUNT_PERCENT}% off!"
    send_sms(message)

    # Write to output for Glide consumption
    write_glide_csv(low_performers, output_csv)
    print(f"Discount CSV written to {output_csv}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Detect low-performing products and trigger discounts")
    parser.add_argument("input_csv", help="Path to CSV with product data")
    parser.add_argument("output_csv", help="Path to CSV for Glide")
    args = parser.parse_args()

    main(args.input_csv, args.output_csv)
