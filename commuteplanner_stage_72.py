# === Stage 72: Add Markdown report export ===
# Project: CommutePlanner
def export_markdown_report(commute):
    lines = []
    lines.append("# Commute Report")
    lines.append("")
    lines.append(f"Total routes tracked: {len(commute['routes'])}")
    lines.append("")
    lines.append("| Route | Avg Delay (min) | Weekly Cost ($) |")
    lines.append("|-------|-----------------|-----------------|")
    for route in commute['routes']:
        avg_delay = sum(route['delays']) / len(route['delays']) if route['delays'] else 0
        weekly_cost = route['cost_per_trip'] * route['trips_per_week']
        lines.append(f"| {route['name']} | {avg_delay:.1f} | {weekly_cost:.2f} |")
    lines.append("")
    total_weekly_cost = sum(r['cost_per_trip'] * r['trips_per_week'] for r in commute['routes'])
    lines.append(f"Total weekly cost across all routes: ${total_weekly_cost:.2f}")
    lines.append("")
    with open(commute['report_path'], 'w') as f:
        f.write("\n".join(lines))
    return commute['report_path']
