# === Stage 24: Add grouped summaries by category or status ===
# Project: CommutePlanner
def grouped_summaries(commute_data):
    """Returns a list of dicts, each dict grouping entries by category or status."""
    grouped = {}
    for entry in commute_data:
        key = entry.get("category", entry.get("status", "unknown"))
        if key not in grouped:
            grouped[key] = []
        grouped[key].append(entry)
    return [{"category": k, "entries": v} for k, v in grouped.items()]
