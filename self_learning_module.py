# Self-Learning Module for AI Profit Suite
# Updates daily with new business skills and suggests an income-generating task.

import json
from datetime import datetime
from pathlib import Path

SKILLS_FILE = Path('skills.json')
PROGRESS_FILE = Path('progress.json')

# Default list of skills and associated tasks
DEFAULT_SKILLS = [
    {
        "skill": "Digital Marketing",
        "task": "Create a social media ad campaign for a local business"
    },
    {
        "skill": "Content Creation",
        "task": "Write a sponsored blog post for a niche audience"
    },
    {
        "skill": "E-commerce Optimization",
        "task": "Analyze a small shop's online sales funnel and suggest improvements"
    },
    {
        "skill": "Email Marketing",
        "task": "Design a lead-nurturing email sequence for a product launch"
    },
    {
        "skill": "SEO Basics",
        "task": "Audit a website's keywords and propose on-page SEO fixes"
    },
]

def load_skills():
    if SKILLS_FILE.exists():
        with SKILLS_FILE.open() as f:
            return json.load(f)
    else:
        with SKILLS_FILE.open('w') as f:
            json.dump(DEFAULT_SKILLS, f, indent=2)
        return DEFAULT_SKILLS

def load_progress():
    if PROGRESS_FILE.exists():
        with PROGRESS_FILE.open() as f:
            return json.load(f)
    return {"last_date": None, "index": -1}

def save_progress(progress):
    with PROGRESS_FILE.open('w') as f:
        json.dump(progress, f, indent=2)

def get_today_skill(skills):
    today = datetime.utcnow().date().isoformat()
    progress = load_progress()

    if progress["last_date"] != today:
        progress["index"] = (progress["index"] + 1) % len(skills)
        progress["last_date"] = today
        save_progress(progress)

    return skills[progress["index"]]

def main():
    skills = load_skills()
    daily = get_today_skill(skills)
    print("Today's business skill:", daily["skill"])
    print("Income-generating task:", daily["task"])

if __name__ == "__main__":
    main()
