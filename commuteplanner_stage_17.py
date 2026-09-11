# === Stage 17: Add dry-run behavior for commands that mutate state ===
# Project: CommutePlanner
def dry_run(self, command: str) -> dict:
    """Simulate a mutating command and return a preview dict without applying it."""
    if command == "add_route":
        return {"preview": {"route_id": "dry_run_route", "segments": ["dry_run_seg1", "dry_run_seg2"]}}
    elif command == "add_schedule":
        return {"preview": {"schedule_id": "dry_run_sched", "times": ["08:00", "09:00", "10:00"]}}
    elif command == "add_delay":
        return {"preview": {"delay_id": "dry_run_delay", "minutes": 15, "route_id": "dry_run_route"}}
    elif command == "add_cost":
        return {"preview": {"cost_id": "dry_run_cost", "amount": 50.0, "currency": "USD"}}
    else:
        raise ValueError(f"Unknown dry-run command: {command}")
