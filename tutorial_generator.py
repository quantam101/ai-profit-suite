import argparse
import datetime
import os
import requests
from bs4 import BeautifulSoup


def fetch_trending_topics(limit: int = 5):
    """Fetch top trending repositories from GitHub."""
    url = "https://github.com/trending"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    repos = []
    for h2 in soup.select("article.Box-row h2")[:limit]:
        repo = " ".join(h2.text.strip().split())
        repos.append(repo)
    return repos


def generate_tutorial_content(topic: str, level: str = "beginner") -> str:
    """Return markdown formatted tutorial template for the topic."""
    if level.lower() == "beginner":
        return (
            f"## {topic} for Beginners\n\n"
            f"This tutorial introduces **{topic}**.\n"
            f"1. Overview of {topic}.\n"
            f"2. Basic setup and simple examples.\n"
            f"3. Additional resources.\n"
        )
    else:
        return (
            f"## Advanced {topic} Guide\n\n"
            f"This tutorial assumes prior experience with **{topic}**.\n"
            f"1. Review of core concepts.\n"
            f"2. Deep dive into advanced features.\n"
            f"3. Best practices and tips.\n"
        )


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate weekly tutorials.")
    parser.add_argument(
        "--topics",
        nargs="*",
        help="Explicit list of topics. If omitted, GitHub trending repositories are used.",
    )
    parser.add_argument(
        "--level",
        choices=["beginner", "expert"],
        default="beginner",
        help="Tutorial difficulty level.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=5,
        help="Number of trending topics to fetch when no topics provided.",
    )
    args = parser.parse_args()

    topics = args.topics if args.topics else fetch_trending_topics(args.limit)
    date_str = datetime.date.today().isoformat()

    os.makedirs("tutorials", exist_ok=True)
    output_path = os.path.join("tutorials", f"{date_str}_{args.level}.md")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(f"# Weekly {args.level.title()} Tutorials - {date_str}\n\n")
        for topic in topics:
            f.write(generate_tutorial_content(topic, args.level))
            f.write("\n")

    print(f"Generated tutorial file: {output_path}")


if __name__ == "__main__":
    main()
