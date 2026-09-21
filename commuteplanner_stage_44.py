# === Stage 44: Add backup creation for the data file ===
# Project: CommutePlanner
def create_backup(source_path, backup_dir="."):
    """Create a timestamped backup of the data file."""
    import os, shutil
    os.makedirs(backup_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    backup_path = os.path.join(backup_dir, os.path.basename(source_path) + f".backup_{timestamp}")
    shutil.copy2(source_path, backup_path)
    return backup_path
