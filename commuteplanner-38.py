# === Stage 38: Add data integrity checks for broken references ===
# Project: CommutePlanner
class ReferenceIntegrityChecker:
    """Validates that all route, schedule, and station references are intact."""
    
    def __init__(self, routes, schedules, stations):
        self.routes = routes
        self.schedules = schedules
        self.stations = stations
    
    def check_routes(self):
        """Ensure every route references valid stations."""
        station_names = {s.name for s in self.stations}
        errors = []
        for i, route in enumerate(self.routes):
            if route.start_station not in station_names:
                errors.append(f"Route {i}: start station '{route.start_station}' not found")
            if route.end_station not in station_names:
                errors.append(f"Route {i}: end station '{route.end_station}' not found")
        return errors
    
    def check_schedules(self):
        """Ensure every schedule references valid routes."""
        route_names = {r.name for r in self.routes}
        errors = []
        for i, schedule in enumerate(self.schedules):
            if schedule.route not in route_names:
                errors.append(f"Schedule {i}: route '{schedule.route}' not found")
        return errors
    
    def check_stations(self):
        """Ensure every station has a valid ID."""
        errors = []
        for i, station in enumerate(self.stations):
            if not station.id:
                errors.append(f"Station {i}: missing ID")
        return errors
    
    def run_all_checks(self):
        """Run all integrity checks and return a summary."""
        route_errors = self.check_routes()
        schedule_errors = self.check_schedules()
        station_errors = self.check_stations()
        
        all_errors = route_errors + schedule_errors + station_errors
        
        if all_errors:
            print("Integrity Check FAILED:")
            for error in all_errors:
                print(f"  - {error}")
            return False
        else:
            print("Integrity Check PASSED: All references are valid.")
            return True
