# AI Profit Suite

This repository contains simple utilities to help convert low-performing products into revenue.

## Detecting Low Performers

Use `detect_and_alert.py` to scan a CSV of product performance and trigger discounts.

```
python detect_and_alert.py products.csv discounts.csv
```

The script checks each product's `units_sold` against the `LOW_PERFORMANCE_THRESHOLD` environment variable (default `10`). Products below this threshold are marked for a flash sale using `DISCOUNT_PERCENT` (default `20`).

If [Twilio](https://www.twilio.com/) is installed and credentials are provided via environment variables, the script sends an SMS summary. It also outputs a CSV (`discounts.csv`) that can be imported into Glide to create flash sale alerts.

### Required Environment Variables for SMS

- `TWILIO_ACCOUNT_SID`
- `TWILIO_AUTH_TOKEN`
- `TWILIO_FROM_NUMBER`
- `TO_NUMBER` (recipient)

### Example Product Data

See `products.csv` for a sample dataset.
