# === Stage 5: Implement update operations with clear handling for missing records ===
# Project: CommutePlanner
def update_record(store, record_type, record_id, updates):
    """Update a single record by key. Returns the updated record or None if not found."""
    if record_type not in store:
        raise KeyError(f"No records of type '{record_type}' found in store")
    if record_id not in store[record_type]:
        raise KeyError(f"Record with id '{record_id}' of type '{record_type}' not found")
    record = store[record_type][record_id]
    for key, value in updates.items():
        if key not in record:
            raise ValueError(f"Cannot update unknown key '{key}' in {record_type} record")
        record[key] = value
    return record
