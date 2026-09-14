# === Stage 27: Add monthly summary calculations ===
# Project: CommutePlanner
def monthly_summary(records):
    """Compute compact monthly summary from commute records.

    Args:
        records: list of dicts with keys like 'month', 'duration', 'cost', 'delay'.

    Returns:
        dict with 'month', 'count', 'avg_duration', 'total_cost', 'avg_cost', 'avg_delay'.
    """
    from collections import defaultdict
    stats = defaultdict(lambda: {'count': 0, 'total_duration': 0, 'total_cost': 0, 'total_delay': 0})
    for r in records:
        m = r.get('month', 'unknown')
        stats[m]['count'] += 1
        stats[m]['total_duration'] += r.get('duration', 0)
        stats[m]['total_cost'] += r.get('cost', 0)
        stats[m]['total_delay'] += r.get('delay', 0)
    result = {}
    for m, s in stats.items():
        result[m] = {
            'count': s['count'],
            'avg_duration': s['total_duration'] / s['count'] if s['count'] else 0,
            'total_cost': s['total_cost'],
            'avg_cost': s['total_cost'] / s['count'] if s['count'] else 0,
            'avg_delay': s['total_delay'] / s['count'] if s['count'] else 0,
        }
    return result
