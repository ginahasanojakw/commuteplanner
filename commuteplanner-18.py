# === Stage 18: Add an activity log with timestamps and action names ===
# Project: CommutePlanner
class ActivityLog:
    def __init__(self):
        self._entries = []

    def log(self, action: str, timestamp: str = None) -> None:
        ts = timestamp or datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self._entries.append({"timestamp": ts, "action": action})

    @property
    def entries(self) -> list:
        return self._entries

    def __len__(self) -> int:
        return len(self._entries)

    def __repr__(self) -> str:
        return f"ActivityLog({len(self._entries)} entries)"
