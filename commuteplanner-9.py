# === Stage 9: Add sorting by title, date, priority, and last update time ===
# Project: CommutePlanner
def sort_entries(entries, key):
    """Sort entries by title, date, priority, or last update time."""
    order = {
        'title': lambda e: e.get('title', ''),
        'date': lambda e: e.get('date', ''),
        'priority': lambda e: e.get('priority', ''),
        'last_update': lambda e: e.get('last_update', ''),
    }
    if key not in order:
        raise ValueError(f"Unknown key: {key}. Use 'title', 'date', 'priority', or 'last_update'.")
    return sorted(entries, key=order[key])
