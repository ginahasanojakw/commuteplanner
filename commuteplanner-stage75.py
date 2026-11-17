# === Stage 75: Add a validation report that lists warnings and errors ===
# Project: CommutePlanner
def validate_schedule(schedule):
    warnings = []
    errors = []
    if not isinstance(schedule, dict):
        return warnings, errors
    routes = schedule.get("routes")
    if not routes:
        warnings.append("No routes defined in schedule.")
    for name, route in routes.items():
        if not isinstance(route, dict):
            errors.append(f"Route '{name}' is not a dictionary.")
            continue
        legs = route.get("legs")
        if not legs:
            warnings.append(f"Route '{name}' has no legs.")
        for i, leg in enumerate(legs):
            if not isinstance(leg, dict):
                errors.append(f"Route '{name}' leg {i} is not a dictionary.")
                continue
            duration = leg.get("duration")
            if duration is None:
                errors.append(f"Route '{name}' leg {i} missing duration.")
            elif duration <= 0:
                warnings.append(f"Route '{name}' leg {i} has non-positive duration.")
            if leg.get("mode") not in ("walk", "bike", "bus", "train", "car"):
                warnings.append(f"Route '{name}' leg {i} has unknown mode.")
            if leg.get("mode") == "bus" or leg.get("mode") == "train":
                delay = leg.get("delay")
                if delay is None:
                    warnings.append(f"Route '{name}' leg {i} missing delay.")
    return warnings, errors
