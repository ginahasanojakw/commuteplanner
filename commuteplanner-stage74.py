# === Stage 74: Add a snapshot comparison helper for before/after states ===
# Project: CommutePlanner
def compare_snapshots(before, after):
    before = before or {}
    after = after or {}
    keys = sorted(set(before) | set(after))
    changes = []
    for key in keys:
        old = before.get(key, None)
        new = after.get(key, None)
        if old != new:
            changes.append({
                "key": key,
                "before": old,
                "after": new,
                "delta": new - old if isinstance(new, (int, float)) and isinstance(old, (int, float)) else None,
            })
    return changes


def summarize_snapshot_changes(before, after):
    changes = compare_snapshots(before, after)
    if not changes:
        return {"status": "unchanged"}
    total_delta = sum(c["delta"] for c in changes if c["delta"] is not None)
    summary = {
        "total_changes": len(changes),
        "total_delta": total_delta,
        "details": changes,
    }
    return summary
