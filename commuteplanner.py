# === Stage 1: Create the base application structure, in-memory state, and a small demo dataset ===
# Project: CommutePlanner
class CommutePlanner:
    def __init__(self):
        self.routes = {}
        self.schedules = {}
        self.delays = {}
        self.costs = {}
        self.demo_routes = [
            ("Home", "Train Station", 15, 5.0),
            ("Train Station", "Work", 30, 1.5),
            ("Home", "Bus Stop", 10, 0.5),
            ("Bus Stop", "Work", 25, 2.0),
        ]
        for src, dst, duration, cost in self.demo_routes:
            self.routes[(src, dst)] = {"duration": duration, "cost": cost}
        self.demo_schedules = {
            "Train Station": [900, 930, 1000, 1030, 1100],
            "Work": [900, 930, 1000, 1030, 1100],
        }
        for stop, times in self.demo_schedules.items():
            self.schedules[stop] = times
        self.demo_delays = {"Train Station": {"avg": 3, "max": 15}}
        self.delays["Train Station"] = self.demo_delays["Train Station"]
