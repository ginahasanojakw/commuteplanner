# === Stage 19: Add undo support for the last simple mutation ===
# Project: CommutePlanner
def undo_last():
    """Undo the last simple mutation by restoring the previous state."""
    if not _undo_stack:
        print("Nothing to undo.")
        return
    previous_state = _undo_stack.pop()
    current_state = _current_state
    if current_state == previous_state:
        print("No change to undo.")
        return
    # Restore previous state
    global _routes, _schedules, _delays, _costs, _current_state
    _routes, _schedules, _delays, _costs, _current_state = previous_state
    print(f"Undo successful. Previous state restored.")
