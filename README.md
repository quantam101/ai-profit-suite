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
