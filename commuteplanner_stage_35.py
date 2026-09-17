# === Stage 35: Add active user switching and user-specific records ===
# Project: CommutePlanner
class User:
    def __init__(self, name):
        self.name = name
        self.commutes = []

    def add_commute(self, commute):
        self.commutes.append(commute)
