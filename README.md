# AI Profit Suite

This repository contains simple utilities for automating alerts using SMS and email. The `alerts.py` script can send a daily notification via Twilio or MailerLite, depending on which credentials are provided.

## Requirements

- Python 3.11+
- [`twilio`](https://pypi.org/project/twilio/)
- [`mailerlite`](https://pypi.org/project/mailerlite/)
- [`schedule`](https://pypi.org/project/schedule/)

Install the dependencies with:

```bash
pip install twilio mailerlite schedule requests
```

## Usage

Set the appropriate environment variables and run the alert scheduler:

```bash
export ALERT_MESSAGE="Your daily reminder"
export ALERT_TIME="09:00"           # 24h format
# Twilio SMS configuration
export TWILIO_ACCOUNT_SID="ACxxxx"
export TWILIO_AUTH_TOKEN="token"
export TWILIO_FROM_NUMBER="+15555555555"
export ALERT_SMS_NUMBER="+15555555555"
# MailerLite email configuration (optional)
export MAILERLITE_API_KEY="key"
export MAILERLITE_GROUP_ID="group_id"
export ALERT_EMAIL="user@example.com"

python alerts.py
```

The script schedules a daily alert at the specified time and sends the message via SMS and/or email depending on the credentials provided.

