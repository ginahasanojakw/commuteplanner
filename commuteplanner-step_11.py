# === Stage 11: Add JSON export for the current application state ===
# Project: CommutePlanner
import json

def export_state(app):
    """Export the full application state to a JSON string."""
    state = {
        "routes": app.routes,
        "schedules": app.schedules,
        "delays": app.delays,
        "costs": app.costs,
        "current_route": app.current_route,
        "current_schedule": app.current_schedule,
        "current_delay": app.current_delay,
        "current_cost": app.current_cost,
        "history": app.history,
    }
    return json.dumps(state, indent=2)
