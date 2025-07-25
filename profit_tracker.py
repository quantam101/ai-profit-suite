import datetime

LOG_FILE = 'profit_log.txt'


def suggest_daily_actions(daily_learnings: str):
    """Return an income-generating action and a business improvement task."""
    insights = daily_learnings.lower()
    income_action = 'Reach out to a potential customer'
    improvement_task = 'Review and refine business processes'

    if 'marketing' in insights or 'seo' in insights:
        income_action = 'Launch a targeted marketing campaign'
    if 'automation' in insights or 'process' in insights:
        improvement_task = 'Automate repetitive tasks'
    return income_action, improvement_task


def log_daily_suggestions(daily_learnings: str, log_file: str = LOG_FILE):
    """Log the suggested actions with the current date."""
    income_action, improvement_task = suggest_daily_actions(daily_learnings)
    date_str = datetime.date.today().isoformat()
    with open(log_file, 'a') as f:
        f.write(f'{date_str} | Income: {income_action} | Improvement: {improvement_task}\n')
    return income_action, improvement_task
