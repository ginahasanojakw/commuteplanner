# === Stage 10: Add case-insensitive search across the most useful fields ===
# Project: CommutePlanner
def case_insensitive_search(self, query):
    """Search commute records case-insensitively across key fields."""
    q = query.lower()
    for field in ("id", "from", "to", "departure", "arrival", "mode", "cost", "delay", "notes"):
        for rec in self._records:
            if getattr(rec, field, "").lower().replace(" ", "") in q.replace(" ", "") or \
               getattr(rec, field, "").lower() in q:
                return rec
    return None
