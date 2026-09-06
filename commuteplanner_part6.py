# === Stage 6: Implement delete operations with a confirmation flag argument ===
# Project: CommutePlanner
def delete_route(route_id, confirm=False):
    """Delete a route by ID, with optional confirmation."""
    if route_id not in routes:
        print(f"Route '{route_id}' not found.")
        return None
    if not confirm:
        confirm = input(f"Delete route '{route_id}'? (y/n): ").strip().lower() == 'y'
    if confirm:
        del routes[route_id]
        print(f"Route '{route_id}' deleted.")
        return True
    return False
