# === Stage 69: Add a reset-demo-data command for manual testing ===
# Project: CommutePlanner
def reset_demo_data():
    """Reset all demo tables to their initial seed values for manual testing."""
    import sqlite3
    from contextlib import closing

    conn = sqlite3.connect("commute.db")
    try:
        cur = conn.cursor()

        cur.execute("DELETE FROM routes")
        cur.execute("DELETE FROM schedules")
        cur.execute("DELETE FROM delays")
        cur.execute("DELETE FROM costs")

        cur.executemany(
            "INSERT INTO routes (id, name, distance_km, duration_min) VALUES (?, ?, ?, ?)",
            [
                (1, "Red Line", 12.5, 30),
                (2, "Blue Line", 8.3, 22),
                (3, "Green Line", 15.1, 38),
            ],
        )

        cur.executemany(
            "INSERT INTO schedules (route_id, weekday, departure_time, arrival_time) VALUES (?, ?, ?, ?)",
            [
                (1, "Mon", "08:00", "08:30"),
                (1, "Tue", "08:00", "08:30"),
                (2, "Wed", "09:15", "09:37"),
                (3, "Thu", "07:45", "08:23"),
            ],
        )

        cur.executemany(
            "INSERT INTO delays (route_id, weekday, delay_min) VALUES (?, ?, ?)",
            [
                (1, "Mon", 5),
                (2, "Wed", 3),
                (3, "Thu", 8),
            ],
        )

        cur.executemany(
            "INSERT INTO costs (route_id, fare_type, cost) VALUES (?, ?, ?)",
            [
                (1, "weekly", 40.0),
                (2, "weekly", 30.0),
                (3, "weekly", 45.0),
            ],
        )

        conn.commit()
        print("Demo data reset.")
    finally:
        with closing(conn):
            pass
