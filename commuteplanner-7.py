# === Stage 7: Add list and detail formatting helpers for console output ===
# Project: CommutePlanner
def format_route(route):
    parts = []
    for stop in route.get('stops', []):
        parts.append(f"{stop['name']} ({stop.get('mode', 'walk')})")
    parts.append(f"Duration: {route.get('duration', 0)} min")
    return " -> ".join(parts)


def format_schedule(schedule):
    lines = [f"Schedule: {schedule.get('name', 'unnamed')}"]
    for trip in schedule.get('trips', []):
        times = trip.get('departures', [])
        line = f"  {times[0] if times else 'N/A'}"
        if len(times) > 1:
            line += f" -> {times[-1]}"
        lines.append(line)
    return "\n".join(lines)


def format_delay_info(delay):
    if delay.get('type') == 'fixed':
        return f"Fixed delay: {delay['value']} min"
    elif delay.get('type') == 'random':
        return f"Random delay: mean={delay['mean']:.1f} min, std={delay['std']:.1f} min"
    return f"Delay: {delay.get('description', 'unknown')}"


def format_cost_summary(trips):
    total_cost = sum(t.get('cost', 0) for t in trips)
    return f"Total trips: {len(trips)}, Total cost: ${total_cost:.2f}"
