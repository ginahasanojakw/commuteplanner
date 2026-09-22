# === Stage 46: Add a schema version field and migration helper ===
# Project: CommutePlanner
import re
from typing import Any

SCHEMA_VERSION = 2


def migrate(data: dict[str, Any], target: int) -> dict[str, Any]:
    """Upgrade data in-place to the requested schema version."""
    if target < SCHEMA_VERSION:
        raise ValueError(f"Cannot downgrade from schema {SCHEMA_VERSION} to {target}")
    if "schema_version" not in data:
        data["schema_version"] = SCHEMA_VERSION
    return data
