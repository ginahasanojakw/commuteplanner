# === Stage 21: Add archive and restore behavior for completed or old records ===
# Project: CommutePlanner
from datetime import datetime, timedelta

def archive_completed_records(records, cutoff_days=30):
    """Archive records older than cutoff_days by setting is_archived=True."""
    cutoff = datetime.now() - timedelta(days=cutoff_days)
    for rec in records:
        if rec.get("completed_at") and rec["completed_at"] < cutoff:
            rec["is_archived"] = True
    return records
