import os
import requests


def fetch_amazon_trending():
    """Fetch trending products from Amazon using the Product Advertising API.

    This requires valid Amazon PA API credentials. Implementation of the full
    signed request is beyond the scope of this example and should follow
    Amazon's official documentation. This function currently serves as a
    placeholder so that users can implement their own compliant solution.
    """
    access_key = os.getenv("AMAZON_ACCESS_KEY")
    secret_key = os.getenv("AMAZON_SECRET_KEY")
    assoc_tag = os.getenv("AMAZON_ASSOC_TAG")
    if not all([access_key, secret_key, assoc_tag]):
        return []
    raise NotImplementedError(
        "Amazon Product Advertising API integration is not implemented."
    )


def fetch_etsy_trending():
    """Fetch trending listings from Etsy using the official API."""
    api_key = os.getenv("ETSY_API_KEY")
    if not api_key:
        return []
    url = f"https://openapi.etsy.com/v2/listings/trending?api_key={api_key}"
    try:
        resp = requests.get(url, timeout=10)
        if resp.status_code != 200:
            return []
        data = resp.json()
    except Exception:
        return []

    results = []
    for item in data.get("results", []):
        results.append({
            "title": item.get("title"),
            "url": item.get("url"),
        })
    return results


def fetch_tiktok_trending():
    """Placeholder for TikTok trending retrieval.

    TikTok does not provide a public API for trending products. Users should
    consult TikTok's terms of service or work with an official data partner
    to obtain this information.
    """
    raise NotImplementedError(
        "TikTok trending API is not publicly available."
    )


def select_top_five(items):
    """Return the first five items from the provided list."""
    return items[:5]


def gather_trending_products():
    products = []

    try:
        products.extend(fetch_amazon_trending())
    except NotImplementedError as e:
        print(e)
    except Exception as e:
        print(f"Amazon fetch failed: {e}")

    try:
        products.extend(fetch_etsy_trending())
    except Exception as e:
        print(f"Etsy fetch failed: {e}")

    try:
        products.extend(fetch_tiktok_trending())
    except NotImplementedError as e:
        print(e)
    except Exception as e:
        print(f"TikTok fetch failed: {e}")

    return select_top_five(products)


if __name__ == "__main__":
    for product in gather_trending_products():
        print(product)
