# === Stage 43: Add CSV import for the primary record type ===
# Project: CommutePlanner
import csv
from datetime import datetime

def import_commutes(filepath):
    """Import commute records from a CSV file."""
    records = []
    with open(filepath, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            record = {
                'date': datetime.strptime(row['date'], '%Y-%m-%d').date(),
                'time': datetime.strptime(row['time'], '%H:%M:%S').time(),
                'route': row['route'],
                'duration': float(row['duration']),
                'delay': float(row['delay']),
                'cost': float(row['cost']),
                'mode': row['mode']
            }
            records.append(record)
    return records
