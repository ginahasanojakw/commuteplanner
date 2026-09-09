# === Stage 13: Add file save support using a configurable path ===
# Project: CommutePlanner
import os
import json

class CommutePlanner:
    def __init__(self):
        self.routes = []
        self.schedule = {}
        self.delays = []
        self.costs = []
        self.data_path = "commute_data.json"

    def save_data(self):
        with open(self.data_path, "w") as f:
            json.dump({
                "routes": self.routes,
                "schedule": self.schedule,
                "delays": self.delays,
                "costs": self.costs
            }, f, indent=2)

    def load_data(self):
        if os.path.exists(self.data_path):
            with open(self.data_path, "r") as f:
                data = json.load(f)
                self.routes = data.get("routes", [])
                self.schedule = data.get("schedule", {})
                self.delays = data.get("delays", [])
                self.costs = data.get("costs", [])
