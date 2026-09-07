# === Stage 8: Add filtering by status, category, owner, or tag ===
# Project: CommutePlanner
def filter_entries(entries, status=None, category=None, owner=None, tag=None):
    """Filter commute entries by status, category, owner, or tag.

    Args:
        entries: list of dicts, each with keys status, category, owner, tag.
        status: optional string to filter by.
        category: optional string to filter by.
        owner: optional string to filter by.
        tag: optional string to filter by.

    Returns:
        A new list containing only the entries that match all provided filters.
    """
    if not entries:
        return []
    result = []
    for entry in entries:
        if status is not None and entry.get("status") != status:
            continue
        if category is not None and entry.get("category") != category:
            continue
        if owner is not None and entry.get("owner") != owner:
            continue
        if tag is not None and entry.get("tag") != tag:
            continue
        result.append(entry)
    return result
