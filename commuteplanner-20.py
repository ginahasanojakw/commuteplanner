# === Stage 20: Add duplicate detection for newly created records ===
# Project: CommutePlanner
def find_duplicates(records, key_field="route_id"):
    seen = {}
    dupes = []
    for r in records:
        k = r.get(key_field)
        if k in seen:
            dupes.append((r, seen[k]))
        else:
            seen[k] = r
    return dupes
