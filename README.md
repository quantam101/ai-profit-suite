
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
=======

# ai-profit-suite

This repository contains simple tools to help grow income through daily skill improvement.

## Self-Learning Module

Run the module to get a new business skill and an income-generating task each day:

```bash
python self_learning_module.py
```

The first run creates `skills.json` and `progress.json` files to track your progress.

=======

# ai-profit-suite

This repository contains the AI Profit Suite application. Run `python main.py` to display the daily self-improvement task.
=======

# ai-profit-suite
=======
# AI Profit Suite

This simple tool helps you track daily learning prompts and rank them based on their usefulness. The program records ratings for each prompt, sorts them by average score, and removes items you mark with a score of `0`.

## Usage

Run the script with Python:

```bash
python3 main.py
```

You will be prompted to rate each learning strategy from 1 (least helpful) to 5 (most helpful). Enter `0` if the prompt was not helpful and should be discarded. After rating, the updated prompt list is saved to `prompts.json` and displayed in ranked order. main


