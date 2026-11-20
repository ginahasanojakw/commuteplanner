# === Stage 80: Polish user-facing messages, names, and examples for consistency ===
# Project: CommutePlanner
def describe_route(route):
    if not route:
        return "No commute planned yet."
    if route["name"] and route["mode"]:
        return f"Your {route['mode'].title()} route is {route['name']}."
    if route["mode"]:
        return f"You usually take the {route['mode'].title()} to work."
    if route["name"]:
        return f"Your commute goes on {route['name']}."
    return "Your commute has no details yet."


def summarize_costs(costs):
    if not costs:
        return "You have not recorded any commute costs yet."
    total = sum(costs.get("amount", 0) for costs in costs)
    label = costs[0]["label"] if costs else "commute"
    return f"This month you spent {total:.2f} on {label}."


def format_delay_message(delay):
    if delay <= 0:
        return "Your commute was on time today."
    if delay < 10:
        return f"Your commute was slightly delayed by {delay} minutes."
    return f"Your commute was delayed by {delay} minutes today."


EXAMPLE_ROUTE = {
    "name": "Blue Line Express",
    "mode": "subway",
    "duration": 32,
    "distance": 14,
}
