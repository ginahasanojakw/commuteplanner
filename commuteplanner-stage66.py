# === Stage 66: Add export of a short status dashboard ===
# Project: CommutePlanner
def export_status_dashboard(commute, days):
    total_cost = sum(commute['costs'][-days:]) if days else sum(commute.get('costs', []))
    total_time = sum(commute['time'][-days:]) if days else sum(commute.get('time', []))
    avg_delay = sum(commute['delay'][-days:]) / days if days and days else 0
    total_distance = sum(commute['distance'][-days:]) if days else sum(commute.get('distance', []))
    lines = ["CommutePlanner Status Dashboard",
             "Cost (avg): ${:.2f}".format(total_cost / days if days else 0),
             "Time (avg): {:.0f} min".format(total_time / days if days else 0),
             "Delay (avg): {:.0f} min".format(avg_delay),
             "Distance (total): {:.0f} km".format(total_distance / 1000 if total_distance else 0)]
    return "\n".join(lines)
