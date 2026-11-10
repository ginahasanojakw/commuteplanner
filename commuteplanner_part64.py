# === Stage 64: Add validation for relationship references ===
# Project: CommutePlanner
def validate_relationships(records):
    """
    Validate that every relationship entry references existing
    people, places, and times. Returns a list of error strings.
    """
    errors = []
    people = {p["id"] for p in records if p.get("type") == "person"}
    places = {pl["id"] for pl in records if pl.get("type") == "place"}
    times = {t["id"] for t in records if t.get("type") == "time"}

    for rel in records:
        if rel.get("type") != "relationship":
            continue
        ref = rel.get("ref")
        kind = rel.get("ref_type")
        if ref is None:
            errors.append(f"Relationship '{rel.get('id')}' has no ref")
            continue
        if kind == "person" and ref not in people:
            errors.append(f"Relationship '{rel.get('id')}' references unknown person '{ref}'")
        elif kind == "place" and ref not in places:
            errors.append(f"Relationship '{rel.get('id')}' references unknown place '{ref}'")
        elif kind == "time" and ref not in times:
            errors.append(f"Relationship '{rel.get('id')}' references unknown time '{ref}'")
        elif kind not in ("person", "place", "time"):
            errors.append(f"Relationship '{rel.get('id')}' has invalid ref_type '{kind}'")

    return errors
