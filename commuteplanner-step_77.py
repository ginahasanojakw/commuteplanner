# === Stage 77: Add type hints to older helper functions that are missing them ===
# Project: CommutePlanner
def estimate_commute_cost(distance_km, fuel_price_per_liter, vehicle_efficiency_km_per_liter, toll_price_per_km=0.0):
    fuel_cost = (distance_km / vehicle_efficiency_km_per_liter) * fuel_price_per_liter
    toll_cost = distance_km * toll_price_per_km
    total_cost = fuel_cost + toll_cost
    return round(total_cost, 2)


def calculate_daily_cost(distance_km, fuel_price_per_liter, vehicle_efficiency_km_per_liter, toll_price_per_km=0.0, trips_per_day=1):
    cost_per_trip = estimate_commute_cost(distance_km, fuel_price_per_liter, vehicle_efficiency_km_per_liter, toll_price_per_km)
    daily_cost = cost_per_trip * trips_per_day
    return round(daily_cost, 2)


def estimate_monthly_cost(daily_cost, days_per_month=22):
    monthly_cost = daily_cost * days_per_month
    return round(monthly_cost, 2)


def estimate_annual_cost(monthly_cost):
    annual_cost = monthly_cost * 12
    return round(annual_cost, 2)


def convert_distance_units(distance_km, to_miles=False):
    if to_miles:
        return round(distance_km * 0.621371, 2)
    return distance_km


def convert_time_units(duration_minutes, to_hours=False):
    if to_hours:
        return round(duration_minutes / 60, 2)
    return duration_minutes


def calculate_delay_penalty(base_time_minutes, delay_minutes, penalty_per_minute=0.5):
    penalty = delay_minutes * penalty_per_minute
    return round(penalty, 2)
