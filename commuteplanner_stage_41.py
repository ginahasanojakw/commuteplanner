# === Stage 41: Add plain text import for a simple line-based format ===
# Project: CommutePlanner
def read_routes_text(filepath):
    """Read routes from a simple line-based text file.
    Each line contains: route_id, start_station, end_station, travel_time_seconds
    Lines starting with '#' are treated as comments.
    """
    routes = []
    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            parts = line.split(',')
            route_id = parts[0].strip()
            start_station = parts[1].strip()
            end_station = parts[2].strip()
            travel_time = int(parts[3].strip())
            routes.append({'route_id': route_id, 'start': start_station, 'end': end_station, 'travel_time': travel_time})
    return routes
