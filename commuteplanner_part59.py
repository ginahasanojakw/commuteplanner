# === Stage 59: Add bulk delete behavior guarded by a confirmation flag ===
# Project: CommutePlanner
def bulk_delete(trips, ids, confirm=False):
    if not confirm:
        raise PermissionError("Bulk delete requires confirm=True")
    remaining = [t for t in trips if t["id"] not in ids]
    deleted = [t for t in trips if t["id"] in ids]
    for trip in deleted:
        trip["deleted"] = True
    return remaining
