# === Stage 67: Add a function that returns key project metrics ===
# Project: CommutePlanner
def get_project_metrics(routes, schedules, delays, costs):
    total_routes = len(routes)
    total_schedules = sum(len(s) for s in schedules)
    total_delays = sum(len(d) for d in delays)
    total_cost = sum(sum(c for c in cost_list) for cost_list in costs)
    avg_delay = (total_delays / total_schedules) if total_schedules else 0.0
    metrics = {
        "total_routes": total_routes,
        "total_schedules": total_schedules,
        "total_delays": total_delays,
        "total_cost": total_cost,
        "avg_delay_minutes": round(avg_delay, 2),
    }
    return metrics
