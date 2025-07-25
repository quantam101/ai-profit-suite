
print("AI Profit Suite Initialized.")


def daily_ai_task():
    """Print today's self-improvement task."""
    print(
        "Today’s task: Improve lead conversion strategy using top-performing keywords."
    )


if __name__ == "__main__":
    daily_ai_task()
=======

"""Entry point for the AI Profit Suite."""


def main() -> None:
    """Run the main routine."""
    print("AI Profit Suite Initialized.")


if __name__ == "__main__":
=======
import json
from pathlib import Path

PROMPT_FILE = Path('prompts.json')

DEFAULT_PROMPTS = [
    {"prompt": "Read documentation for 30 minutes", "ratings": []},
    {"prompt": "Complete a coding challenge", "ratings": []},
    {"prompt": "Watch a tutorial video", "ratings": []}
]

def load_prompts():
    if PROMPT_FILE.exists():
        with PROMPT_FILE.open('r') as f:
            return json.load(f)
    else:
        with PROMPT_FILE.open('w') as f:
            json.dump(DEFAULT_PROMPTS, f, indent=2)
        return DEFAULT_PROMPTS


def save_prompts(prompts):
    with PROMPT_FILE.open('w') as f:
        json.dump(prompts, f, indent=2)


def get_score(prompt):
    ratings = prompt.get('ratings', [])
    return sum(ratings) / len(ratings) if ratings else 0


def ask_for_ratings(prompts):
    updated = []
    for p in prompts:
        print(f"\nPrompt: {p['prompt']}")
        try:
            rating = int(input("Rate from 1-5 (0 to remove): "))
        except ValueError:
            print("Invalid input, skipping")
            continue
        if rating == 0:
            continue  # discard prompt
        p.setdefault('ratings', []).append(rating)
        p['score'] = get_score(p)
        updated.append(p)
    updated.sort(key=lambda x: x.get('score', 0), reverse=True)
    return updated


def display_prompts(prompts):
    print("\nRanked strategies:")
    for p in prompts:
        score = get_score(p)
        print(f"- {p['prompt']} (score: {score:.2f})")


def main():
    print("AI Profit Suite Initialized.")
    prompts = load_prompts()
    prompts = ask_for_ratings(prompts)
    save_prompts(prompts)
    display_prompts(prompts)


if __name__ == '__main__':

    main()

