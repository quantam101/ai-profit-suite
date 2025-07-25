codex/generate-daily-earnings-summary-report
# AI Profit Suite

This repository contains simple utilities for tracking and communicating daily business metrics.

## Scripts

### `daily_summary.py`
Sends a daily summary via SMS using the Twilio API. The script expects a JSON file with the following structure:

```json
{
  "date": "2024-07-25",
  "earnings": 250.50,
  "traffic_sources": {
    "google": 120,
    "facebook": 80
  },
  "actions_taken": [
    "Updated product page",
    "Launched ad campaign"
  ]
}
```

The message is formatted and sent to the configured phone number.

#### Usage
1. Install dependencies:
   ```bash
   pip install twilio
   ```
2. Set Twilio credentials and phone numbers as environment variables:
   - `TWILIO_ACCOUNT_SID`
   - `TWILIO_AUTH_TOKEN`
   - `TWILIO_FROM_NUMBER`
   - `TWILIO_TO_NUMBER`
3. Run the script with your data file:
   ```bash
   python daily_summary.py sample_data.json
   ```

### `main.py`
Simple placeholder script that prints a message when executed.
=======
codex/add-user-upload-functionality-for-resources
# AI Profit Suite

This repository provides utilities for managing shared resources.

## Uploading Resources

Use `python main.py upload <path-or-url>` to add a guide, file, or link to the
`shared_resources` directory. The command will copy local files or create a
`.url` file containing the link.

Example:

```bash
python main.py upload https://example.com/guide
```
=======

# AI Profit Suite

This project demonstrates how to gather trending product information from
supported platforms using official APIs. It also shows how to combine these
results to highlight the top items to promote.

## Requirements

- Python 3.8+
- `requests` library (`pip install requests`)
- API credentials for any services you want to query (e.g. Amazon PA API,
  Etsy API). TikTok's trending data is not fetched because a public API is not
  available.

## Usage

1. Set the environment variables for the services you wish to enable:

   ```bash
   export ETSY_API_KEY=your_etsy_key
   export AMAZON_ACCESS_KEY=your_amazon_key
   export AMAZON_SECRET_KEY=your_amazon_secret
   export AMAZON_ASSOC_TAG=your_amazon_associate_tag
   ```

   TikTok trending retrieval is not implemented; consult TikTok's terms of
   service for approved methods.

2. Run the suite:

   ```bash
   python main.py
   ```

The script will attempt to fetch trending items and print up to five products to
consider promoting.
=======

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



main
main
