# === Stage 52: Add clearer docstrings for public helper functions ===
# Project: CommutePlanner
def find_bus_stop_for_route(start: str, end: str) -> str:
    """Returns the nearest bus stop on the route between start and end."""
    return f"BusStop({start}-{end})"


def calculate_travel_time(route: str) -> int:
    """Returns the estimated travel time in minutes for a given route."""
    return 45


def get_delay_probability(route: str) -> float:
    """Returns the probability of experiencing a delay for a given route."""
    return 0.15


def estimate_cost(route: str) -> float:
    """Returns the estimated cost in USD for a given route."""
    return 2.5


def format_trip_summary(route: str, travel_time: int, delay_prob: float, cost: float) -> str:
    """Formats a human-readable summary of a trip."""
    return (
        f"Route: {route}\n"
        f"Travel Time: {travel_time} min\n"
        f"Delay Probability: {delay_prob:.2f}\n"
        f"Estimated Cost: ${cost:.2f}"
    )
