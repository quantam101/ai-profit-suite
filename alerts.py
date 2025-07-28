# Daily alert script for AI Profit Suite
# Uses Twilio for SMS and MailerLite for email

import os
import time
from datetime import datetime

import schedule
from twilio.rest import Client
import requests


def send_sms(message: str, to_number: str | None = None) -> None:
    """Send an SMS message via Twilio."""
    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    from_number = os.getenv("TWILIO_FROM_NUMBER")
    to_number = to_number or os.getenv("ALERT_SMS_NUMBER")
    if not all([account_sid, auth_token, from_number, to_number]):
        raise RuntimeError("Twilio configuration is incomplete.")
    client = Client(account_sid, auth_token)
    client.messages.create(body=message, from_=from_number, to=to_number)


def send_mailerlite_email(subject: str, content: str, to_email: str | None = None) -> None:
    """Send an email via MailerLite."""
    api_key = os.getenv("MAILERLITE_API_KEY")
    group_id = os.getenv("MAILERLITE_GROUP_ID")
    to_email = to_email or os.getenv("ALERT_EMAIL")
    if not all([api_key, group_id, to_email]):
        raise RuntimeError("MailerLite configuration is incomplete.")
    headers = {
        "X-MailerLite-ApiKey": api_key,
        "Content-Type": "application/json",
    }
    data = {
        "subject": subject,
        "body": content,
        "groups": [group_id],
        "emails": [to_email],
    }
    response = requests.post(
        "https://api.mailerlite.com/api/v2/email/send",
        json=data,
        headers=headers,
        timeout=10,
    )
    response.raise_for_status()


def send_daily_alert() -> None:
    """Send the daily alert via SMS and/or email."""
    message = os.getenv("ALERT_MESSAGE", f"Daily update {datetime.now().date()}")
    if os.getenv("TWILIO_ACCOUNT_SID"):
        send_sms(message)
    if os.getenv("MAILERLITE_API_KEY"):
        send_mailerlite_email("Daily Alert", message)


def main() -> None:
    alert_time = os.getenv("ALERT_TIME", "09:00")
    schedule.every().day.at(alert_time).do(send_daily_alert)
    print(f"Daily alert scheduled at {alert_time}")
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
