# === Stage 33: Add a settings dictionary and functions to update settings ===
# Project: CommutePlanner
def get_settings():
    return {
        'max_delay_minutes': 15,
        'min_cost_per_km': 0.15,
        'preferred_departure_hour': 7,
        'avoid_highway': False,
        'show_alternatives': True,
    }

def update_settings(settings, **kwargs):
    for key, value in kwargs.items():
        if key in settings:
            settings[key] = value
        else:
            raise KeyError(f"Unknown setting: {key}")
    return settings

def reset_settings():
    return get_settings()
