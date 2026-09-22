# === Stage 45: Add restore from backup with validation ===
# Project: CommutePlanner
def restore_from_backup(backup_file):
    if not backup_file.exists():
        raise FileNotFoundError(f"Backup file not found: {backup_file}")
    try:
        with open(backup_file, 'r') as f:
            data = json.load(f)
        for key in ('routes', 'schedules', 'delays', 'costs'):
            if key not in data:
                raise ValueError(f"Missing key in backup: {key}")
        return data
    except json.JSONDecodeError:
        raise ValueError("Backup file contains invalid JSON")
