# === Stage 36: Add templates for quickly creating common records ===
# Project: CommutePlanner
class RecordTemplates:
    """Factory for common record types used throughout CommutePlanner."""

    @staticmethod
    def daily_schedule():
        return {
            "date": None,
            "departure_time": None,
            "arrival_time": None,
            "duration": None,
            "mode": None,
        }

    @staticmethod
    def route():
        return {
            "name": None,
            "start": None,
            "end": None,
            "distance": None,
            "estimated_time": None,
            "mode": None,
        }

    @staticmethod
    def commute_record():
        return {
            "date": None,
            "departure_time": None,
            "arrival_time": None,
            "mode": None,
            "distance": None,
            "cost": None,
            "delays": [],
        }

    @staticmethod
    def delay_record():
        return {
            "date": None,
            "route": None,
            "duration": None,
            "cause": None,
            "severity": None,
        }

    @staticmethod
    def cost_summary():
        return {
            "date": None,
            "total_cost": None,
            "fuel_cost": None,
            "maintenance_cost": None,
            "parking_cost": None,
            "other": None,
        }
