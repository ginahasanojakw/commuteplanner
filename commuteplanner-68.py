# === Stage 68: Add a compact changelog generated from the activity log ===
# Project: CommutePlanner
def build_changelog(log):
    """Generate a compact changelog from the activity log."""
    lines = []
    lines.append("CommutePlanner Changelog")
    lines.append("=" * 25)
    for entry in log:
        date, title = entry["date"], entry["title"]
        lines.append(f"- {date}: {title}")
    return "\n".join(lines)
