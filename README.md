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
