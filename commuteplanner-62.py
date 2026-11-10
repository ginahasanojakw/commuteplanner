# === Stage 62: Add simple scoring or priority recommendation logic ===
# Project: CommutePlanner
def recommend_routes(routes):
    scored = []
    for route in routes:
        travel_time = route.get_travel_time()
        cost = route.get_cost()
        comfort = route.get_comfort_score()
        delay_penalty = route.get_average_delay()
        score = (comfort * 0.4) - (delay_penalty * 0.3) - (cost * 0.2) - (travel_time * 0.1)
        scored.append((score, route))
    scored.sort(key=lambda x: x[0], reverse=True)
    return scored[:3]
