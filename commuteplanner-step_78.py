# === Stage 78: Refactor one large function into smaller helpers while preserving behavior ===
# Project: CommutePlanner
def split_schedule(schedule):
    """Split a schedule string into individual trips."""
    return [trip.strip() for trip in schedule.split(';') if trip.strip()]


def parse_trip(trip):
    """Parse a single trip string into a structured dict."""
    parts = trip.split('|')
    return {
        'mode': parts[0] if len(parts) > 0 else 'unknown',
        'departure': parts[1] if len(parts) > 1 else None,
        'arrival': parts[2] if len(parts) > 2 else None,
        'duration': parts[3] if len(parts) > 3 else None,
    }


def calculate_delay(actual_departure, expected_departure):
    """Calculate delay in minutes between actual and expected departure."""
    actual = datetime.strptime(actual_departure, '%H:%M')
    expected = datetime.strptime(expected_departure, '%H:%M')
    delta = actual - expected
    return delta.total_seconds() / 60


def calculate_trip_cost(trips, cost_per_km):
    """Calculate total cost for a list of trips based on distance."""
    total_cost = 0
    for trip in trips:
        distance = float(trip.get('distance', 0))
        total_cost += distance * cost_per_km
    return total_cost


def summarize_commuting(schedules, cost_per_km):
    """Summarize commuting data with trip counts, delays, and costs."""
    all_trips = [parse_trip(trip) for trip in split_schedule(schedules)]
    total_delay = sum(calculate_delay(t['departure'], t['expected_departure']) for t in all_trips)
    total_cost = calculate_trip_cost(all_trips, cost_per_km)
    return {
        'total_trips': len(all_trips),
        'total_delay_minutes': total_delay,
        'total_cost': total_cost,
    }
