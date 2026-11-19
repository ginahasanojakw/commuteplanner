# === Stage 79: Add a final self-check command that runs validations and demo operations ===
# Project: CommutePlanner
def main():
    planner = CommutePlanner()
    route = planner.add_route("Red Line", ["Home", "Transit Hub", "Office"])
    schedule = planner.add_schedule("Red Line", [("7:00", "7:25"), ("8:00", "8:25")])
    planner.add_delay("Red Line", "7:25", 15)
    planner.add_cost("Red Line", 5.0)
    print("Routes:", planner.list_routes())
    print("Schedules:", planner.list_schedules())
    print("Route 'Red Line':", planner.get_route("Red Line"))
    print("Delays:", planner.get_delays("Red Line"))
    print("Cost:", planner.get_cost("Red Line"))
    print("Latest departure:", planner.latest_departure("Red Line"))
    for name, r in planner.list_routes().items():
        assert len(r.stops) >= 2, "Route needs at least two stops"
        assert planner.get_cost(name) is not None, "Route needs a cost"
    assert planner.latest_departure("Red Line") == "8:00"
    assert planner.get_delays("Red Line") == [("7:25", 15)]
    print("All checks passed.")

if __name__ == "__main__":
    main()
