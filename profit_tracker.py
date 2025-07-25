class ProfitTracker:
    def __init__(self):
        self.daily_revenue = []

    def log_profit(self, amount):
        self.daily_revenue.append(amount)
        print(f"Logged: ${amount} | Total: ${sum(self.daily_revenue)}")

    def average_profit(self):
        return sum(self.daily_revenue) / len(self.daily_revenue) if self.daily_revenue else 0
