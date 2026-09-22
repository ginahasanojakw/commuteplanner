# === Stage 47: Add a demo scenario that exercises the main workflow ===
# Project: CommutePlanner
def demo():
    planner = CommutePlanner("Home", "Office")
    routes = [
        Route("Route A", "Bus", "45", "1.80"),
        Route("Route B", "Train", "35", "2.20"),
        Route("Route C", "Bike", "20", "0.00"),
    ]
    planner.load_routes(routes)
    schedule = planner.get_schedule("Route A", "08:00")
    print(f"Departure: 08:00, Arrival: {schedule['arrival']}, Duration: {schedule['duration']}min")
    delays = planner.get_delays("Route A", "08:00", "09:00")
    print(f"Delays: {delays}")
    cost = planner.get_cost("Route A")
    print(f"Cost: {cost}")
    planner.find_best_route("Route A", "Route B", "Route C")
    print("Best route selected.")
