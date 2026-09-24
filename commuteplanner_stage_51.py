# === Stage 51: Add unit tests for search and filter behavior ===
# Project: CommutePlanner
import unittest
from commute_planner.models.route import Route
from commute_planner.models.schedule import Schedule
from commute_planner.models.delay import Delay
from commute_planner.models.cost import Cost
from commute_planner.services.search import SearchService
from commute_planner.services.filter import FilterService

class TestSearchFilter(unittest.TestCase):
    def setUp(self):
        self.search = SearchService()
        self.filter = FilterService()

    def test_search_routes_by_destination(self):
        routes = [
            Route(id=1, name="Bus 1", mode="bus", origin="Home", destination="Work"),
            Route(id=2, name="Train 1", mode="train", origin="Home", destination="Work"),
            Route(id=3, name="Bus 2", mode="bus", origin="Home", destination="School"),
        ]
        results = self.search.search_routes(routes, destination="Work")
        self.assertEqual(len(results), 2)
        self.assertEqual({r.id for r in results}, {1, 2})

    def test_search_schedules_by_date(self):
        schedules = [
            Schedule(id=1, route_id=1, departure="08:00", arrival="09:00", date="2024-01-15"),
            Schedule(id=2, route_id=1, departure="09:00", arrival="10:00", date="2024-01-15"),
            Schedule(id=3, route_id=2, departure="08:00", arrival="08:30", date="2024-01-15"),
        ]
        results = self.search.search_schedules(schedules, date="2024-01-15")
        self.assertEqual(len(results), 3)

    def test_filter_delays_by_severity(self):
        delays = [
            Delay(id=1, route_id=1, severity="minor", duration_minutes=5),
            Delay(id=2, route_id=1, severity="major", duration_minutes=15),
            Delay(id=3, route_id=2, severity="minor", duration_minutes=3),
        ]
        results = self.filter.filter_delays(delays, severity="major")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].id, 2)

    def test_filter_costs_by_mode(self):
        costs = [
            Cost(id=1, route_id=1, mode="bus", amount=2.50),
            Cost(id=2, route_id=1, mode="train", amount=4.00),
            Cost(id=3, route_id=2, mode="bus", amount=2.50),
        ]
        results = self.filter.filter_costs(costs, mode="train")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].amount, 4.00)

if __name__ == "__main__":
    unittest.main()
