# === Stage 71: Add a seed-demo-data helper with deterministic sample data ===
# Project: CommutePlanner
def seed_demo_data():
    routes = [
        {
            "id": "R1",
            "name": "Downtown Loop",
            "segments": [
                {"mode": "walk", "duration": 5, "delay": 0},
                {"mode": "subway", "duration": 20, "delay": 3},
                {"mode": "bus", "duration": 10, "delay": 2},
            ],
        },
        {
            "id": "R2",
            "name": "Express Line",
            "segments": [
                {"mode": "walk", "duration": 3, "delay": 0},
                {"mode": "train", "duration": 25, "delay": 0},
            ],
        },
        {
            "id": "R3",
            "name": "Bike Path",
            "segments": [
                {"mode": "bike", "duration": 15, "delay": 0},
            ],
        },
    ]
    schedules = [
        {"route_id": "R1", "departure_time": "08:00", "arrival_time": "08:32"},
        {"route_id": "R2", "departure_time": "08:10", "arrival_time": "08:35"},
        {"route_id": "R3", "departure_time": "08:15", "arrival_time": "08:30"},
    ]
    costs = [
        {"route_id": "R1", "fare": 3.50},
        {"route_id": "R2", "fare": 2.75},
        {"route_id": "R3", "fare": 0.00},
    ]
    return {"routes": routes, "schedules": schedules, "costs": costs}
