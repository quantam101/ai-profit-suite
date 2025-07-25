import argparse
from pytrends.request import TrendReq


def google_trends_regions(keyword: str, geo: str = "US", timeframe: str = "today 12-m"):
    """Return region interest for the given keyword."""
    pytrends = TrendReq()
    pytrends.build_payload([keyword], geo=geo, timeframe=timeframe)
    data = pytrends.interest_by_region(resolution="CITY", inc_low_vol=True, inc_geo_code=True)
    # Sort from highest to lowest interest
    return data.sort_values(by=keyword, ascending=False)


def main():
    parser = argparse.ArgumentParser(description="Find best regions for business expansion using Google Trends")
    parser.add_argument("keyword", help="Search term to analyze")
    parser.add_argument("--top", type=int, default=10, help="Number of top regions to display")
    parser.add_argument("--geo", default="US", help="Geographical area code, e.g., US")
    parser.add_argument("--timeframe", default="today 12-m", help="Timeframe for trends query")
    args = parser.parse_args()

    df = google_trends_regions(args.keyword, geo=args.geo, timeframe=args.timeframe)
    print(df.head(args.top))


if __name__ == "__main__":
    main()
