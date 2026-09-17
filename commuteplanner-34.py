# === Stage 34: Add support for multiple local user profiles ===
# Project: CommutePlanner
import json
import os

USER_PROFILES_DIR = os.path.join(os.path.expanduser("~"), ".commutepanner", "profiles")

def get_user_profiles():
    """Load all local user profiles from JSON files in the profiles directory."""
    os.makedirs(USER_PROFILES_DIR, exist_ok=True)
    profiles = {}
    if os.path.isdir(USER_PROFILES_DIR):
        for fname in os.listdir(USER_PROFILES_DIR):
            if fname.endswith(".json"):
                filepath = os.path.join(USER_PROFILES_DIR, fname)
                try:
                    with open(filepath, "r") as f:
                        data = json.load(f)
                        name = data.get("name", fname.replace(".json", ""))
                        profiles[name] = data
                except (json.JSONDecodeError, IOError):
                    pass
    return profiles
