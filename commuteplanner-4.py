# === Stage 4: Implement create operations for the primary records ===
# Project: CommutePlanner
def create_route(self, name, points, travel_time=None):
    """Register a new route with a name and ordered (lat, lon) points."""
    if not points:
        raise ValueError("A route needs at least one point.")
    self.routes[name] = {
        "name": name,
        "points": points,
        "travel_time": travel_time,
        "created": datetime.now(),
    }
    return self.routes[name]
