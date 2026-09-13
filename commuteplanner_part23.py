# === Stage 23: Add tag add/remove helpers and tag-based summaries ===
# Project: CommutePlanner
def add_tag(commute, tag):
    """Add a tag to a commute entry."""
    if tag not in commute.tags:
        commute.tags.append(tag)

def remove_tag(commute, tag):
    """Remove a tag from a commute entry."""
    if tag in commute.tags:
        commute.tags.remove(tag)

def summarize_by_tags(commutes, tags=None):
    """Return summary statistics grouped by tags."""
    if tags is None:
        tags = set()
    summary = {}
    for commute in commutes:
        for tag in commute.tags:
            if tag in tags:
                if tag not in summary:
                    summary[tag] = {'count': 0, 'total_cost': 0, 'total_time': 0}
                summary[tag]['count'] += 1
                summary[tag]['total_cost'] += commute.cost
                summary[tag]['total_time'] += commute.duration
    return summary
