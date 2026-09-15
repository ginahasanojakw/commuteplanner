# === Stage 29: Add reminder helpers that return upcoming items ===
# Project: CommutePlanner
def get_upcoming_items(schedules, now=None):
    """Return sorted list of upcoming schedule items."""
    if now is None:
        now = datetime.now()
    upcoming = []
    for s in schedules:
        if s['time'] > now:
            upcoming.append(s)
    upcoming.sort(key=lambda x: x['time'])
    return upcoming

def format_upcoming_text(upcoming, max_items=5):
    """Format upcoming items as a human-readable string."""
    if not upcoming:
        return "No upcoming items."
    text = "Upcoming items:\n"
    for item in upcoming[:max_items]:
        text += f"  - {item['description']} at {item['time'].strftime('%Y-%m-%d %H:%M')}\n"
    if len(upcoming) > max_items:
        text += f"  ... and {len(upcoming) - max_items} more\n"
    return text
