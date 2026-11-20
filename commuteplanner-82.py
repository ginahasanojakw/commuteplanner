# === Stage 82: Add an end-to-end demo function that prints a complete walkthrough ===
# Project: CommutePlanner
def demo():
    routes = {
        "Red Line": {
            "stops": ["Central", "Riverside", "Harbor"],
            "headway_min": 10,
            "cost": 2.5,
        },
        "Blue Line": {
            "stops": ["Central", "Airport", "Downtown"],
            "headway_min": 15,
            "cost": 3.0,
        },
    }
    schedule = {
        "Red Line": [
            {"departure": "08:00", "arrival": "08:12", "delay_min": 0},
            {"departure": "08:10", "arrival": "08:23", "delay_min": 3},
        ]
    }
    trips = []
    for route in routes:
        cost = routes[route]["cost"]
        for trip in schedule.get(route, []):
            duration = (trip["arrival"] - trip["departure"]).total_seconds() / 60.0
            trips.append(
                {
                    "route": route,
                    "departure": trip["departure"],
                    "duration": duration,
                    "delay": trip["delay_min"],
                    "cost": cost,
                }
            )
    total_cost = sum(t["cost"] for t in trips)
    total_delay = sum(t["delay"] for t in trips)
    print("CommutePlanner End-to-End Demo")
    print("Routes:", list(routes.keys()))
    print("Trips:")
    for t in trips:
        print(
            " -",
            t["route"],
            "departs",
            t["departure"],
            "duration",
            t["duration"],
            "min",
            "delay",
            t["delay"],
            "min",
            "cost",
            t["cost"],
        )
    print("Total cost:", round(total_cost, 2))
    print("Total delay:", total_delay, "min")
