# === Stage 63: Add relationships between records where useful ===
# Project: CommutePlanner
def add_relationships(records):
    """Attach relationships to records where useful."""
    for record in records:
        rid = record["id"]
        record["relationships"] = {}
        for other in records:
            if other["id"] == rid or not other.get("links_to", False):
                continue
            rel = other["links_to"]
            if rel in ("uses_route", "on_schedule_for", "incurs_delay_for", "tracked_cost_for"):
                record["relationships"].setdefault(rel, []).append(other["id"])
        return record
