import json
import os
from datetime import datetime
from twilio.rest import Client


def load_data(file_path: str) -> dict:
    with open(file_path, 'r') as f:
        return json.load(f)


def format_summary(data: dict) -> str:
    date = data.get("date", datetime.now().strftime("%Y-%m-%d"))
    earnings = data.get("earnings", 0)
    traffic_sources = data.get("traffic_sources", {})
    actions = data.get("actions_taken", [])

    sources_sorted = sorted(traffic_sources.items(), key=lambda x: x[1], reverse=True)
    top_sources = ", ".join(f"{source}: {visits}" for source, visits in sources_sorted)
    actions_str = "; ".join(actions)

    message = (
        f"Daily Summary for {date}\n"
        f"Earnings: ${earnings}\n"
        f"Top Traffic Sources: {top_sources}\n"
        f"Actions Taken: {actions_str}"
    )
    return message


def send_sms(body: str) -> None:
    account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
    auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
    from_number = os.environ.get('TWILIO_FROM_NUMBER')
    to_number = os.environ.get('TWILIO_TO_NUMBER')

    if not all([account_sid, auth_token, from_number, to_number]):
        raise EnvironmentError("Twilio credentials or phone numbers are missing")

    client = Client(account_sid, auth_token)
    client.messages.create(body=body, from_=from_number, to=to_number)


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Send daily business summary via SMS")
    parser.add_argument('data_file', help="Path to JSON file containing summary data")
    parser.add_argument('--dry-run', action='store_true', help="Print the summary instead of sending an SMS")
    args = parser.parse_args()

    data = load_data(args.data_file)
    summary = format_summary(data)
    if args.dry_run:
        print(summary)
    else:
        send_sms(summary)
        print("Summary sent successfully.")


if __name__ == '__main__':
    main()
