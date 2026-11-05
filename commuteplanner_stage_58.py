# === Stage 58: Add bulk update behavior for selected records ===
# Project: CommutePlanner
def bulk_update(records, fields, mapping):
    for record in records:
        for field, value in mapping.items():
            if field in fields and getattr(record, field) is not value:
                setattr(record, field, value)
    return records
