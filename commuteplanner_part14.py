# === Stage 14: Add file load support with fallback demo data ===
# Project: CommutePlanner
try:
    import pickle
    with open("commute_data.pkl", "rb") as f:
        data = pickle.load(f)
except (FileNotFoundError, Exception):
    data = {
        "routes": [
            {"id": "r1", "name": "Downtown Express", "stops": 5, "duration_min": 25, "cost": 2.50},
            {"id": "r2", "name": "Suburban Shuttle", "stops": 8, "duration_min": 40, "cost": 1.75},
            {"id": "r3", "name": "Night Owl", "stops": 3, "duration_min": 18, "cost": 3.00},
        ],
        "delays": [
            {"route_id": "r1", "date": "2024-01-15", "delay_min": 12},
            {"route_id": "r2", "date": "2024-01-15", "delay_min": 5},
            {"route_id": "r1", "date": "2024-01-16", "delay_min": 0},
        ],
        "costs": [
            {"route_id": "r1", "date": "2024-01-15", "cost": 2.80},
            {"route_id": "r2", "date": "2024-01-15", "cost": 1.90},
            {"route_id": "r1", "date": "2024-01-16", "cost": 2.50},
        ]
    }
