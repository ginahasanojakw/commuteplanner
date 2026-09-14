# === Stage 26: Add weekly summary calculations ===
# Project: CommutePlanner
def weekly_summary(data):
    """Compute a simple weekly summary from daily commute records."""
    weeks = {}
    for day in data:
        w = day["date"].strftime("%Y-W%W")
        weeks.setdefault(w, {"days": 0, "total_time": 0, "total_cost": 0, "delays": 0})
        weeks[w]["days"] += 1
        weeks[w]["total_time"] += day["time"]
        weeks[w]["total_cost"] += day["cost"]
        if day.get("delay"):
            weeks[w]["delays"] += 1
    return weeks
