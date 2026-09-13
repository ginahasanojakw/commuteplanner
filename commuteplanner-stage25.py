# === Stage 25: Add daily summary calculations ===
# Project: CommutePlanner
import statistics

def daily_summary(records):
    """Compute a daily summary of commute records.

    Args:
        records: List of dictionaries with keys 'date', 'duration', 'cost',
                  'delays', 'mode'.

    Returns:
        Dictionary with daily averages, totals, and min/max values.
    """
    daily = {}
    for r in records:
        date = r['date']
        if date not in daily:
            daily[date] = {
                'durations': [],
                'costs': [],
                'delays': [],
                'modes': [],
            }
        daily[date]['durations'].append(r['duration'])
        daily[date]['costs'].append(r['cost'])
        daily[date]['delays'].append(r['delays'])
        daily[date]['modes'].append(r['mode'])

    summary = {}
    for date, vals in daily.items():
        summary[date] = {
            'avg_duration': statistics.mean(vals['durations']),
            'total_cost': sum(vals['costs']),
            'total_delays': sum(vals['delays']),
            'avg_delays': statistics.mean(vals['delays']),
            'min_duration': min(vals['durations']),
            'max_duration': max(vals['durations']),
            'mode_count': {m: vals['modes'].count(m) for m in set(vals['modes'])},
        }
    return summary
