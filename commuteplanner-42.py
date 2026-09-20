# === Stage 42: Add CSV export without external dependencies ===
# Project: CommutePlanner
import csv

def export_commute_to_csv(commute_data, filename='commute_export.csv'):
    """Export commute data to CSV without external dependencies.

    Args:
        commute_data: List of dicts with commute info.
        filename: Output CSV file name.

    Returns:
        Number of rows exported.
    """
    if not commute_data:
        return 0

    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=commute_data[0].keys())
        writer.writeheader()
        writer.writerows(commute_data)

    return len(commute_data)
