from profit_tracker import log_daily_suggestions

print("AI Profit Suite Initialized.")

daily_learnings = input("Describe today's learning: ")

income_action, improvement_task = log_daily_suggestions(daily_learnings)

print("Income-generating action:", income_action)
print("Business improvement task:", improvement_task)
