# === Stage 15: Add a simple command dispatcher for text commands ===
# Project: CommutePlanner
def dispatch_command(cmd: str) -> str:
    """Parse a short text command and return a human-readable response."""
    cmd = cmd.strip().lower()
    if cmd == "routes":
        return "Available routes: express, local, bus, subway, taxi, bike."
    elif cmd == "schedule":
        return "Express: 7:00, 8:00, 9:00. Local: 6:30, 7:15, 8:30. Bus: 7:00, 7:30, 8:00. Subway: 6:45, 7:45, 8:45. Taxi: on-demand. Bike: any time."
    elif cmd == "delays":
        return "No active delays reported."
    elif cmd == "cost":
        return "Express: $12. Local: $6. Bus: $4. Subway: $5. Taxi: $15. Bike: free."
    elif cmd == "status":
        return "System online. Last update: 2026-05-17."
    elif cmd == "help":
        return "Commands: routes, schedule, delays, cost, status, help."
    elif cmd == "quit":
        return "Goodbye!"
    else:
        return f"Unknown command: {cmd}. Try 'help'."
