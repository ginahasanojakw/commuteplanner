# === Stage 39: Add a repair function for simple data integrity issues ===
# Project: CommutePlanner
def repair_data_integrity(data):
    """
    Repair simple data integrity issues in the commute data dictionary.
    
    Parameters:
    data (dict): The commute data dictionary containing routes, schedules, delays, and costs.
    
    Returns:
    dict: The repaired data dictionary.
    """
    # Ensure all required keys are present
    required_keys = ['routes', 'schedules', 'delays', 'costs']
    for key in required_keys:
        if key not in data:
            data[key] = {}

    # Repair route data: ensure each route has required attributes
    for route_id, route in data['routes'].items():
        if 'distance' not in route:
            route['distance'] = 0.0
        if 'duration' not in route:
            route['duration'] = 0.0
        if 'route_type' not in route:
            route['route_type'] = 'unknown'

    # Repair schedule data: ensure each schedule has required attributes
    for schedule_id, schedule in data['schedules'].items():
        if 'departure_time' not in schedule:
            schedule['departure_time'] = '00:00'
        if 'arrival_time' not in schedule:
            schedule['arrival_time'] = '00:00'
        if 'frequency' not in schedule:
            schedule['frequency'] = 'daily'

    # Repair delay data: ensure each delay has required attributes
    for delay_id, delay in data['delays'].items():
        if 'delay_minutes' not in delay:
            delay['delay_minutes'] = 0
        if 'delay_type' not in delay:
            delay['delay_type'] = 'minor'

    # Repair cost data: ensure each cost has required attributes
    for cost_id, cost in data['costs'].items():
        if 'amount' not in cost:
            cost['amount'] = 0.0
        if 'cost_type' not in cost:
            cost['cost_type'] = 'fixed'

    return data
