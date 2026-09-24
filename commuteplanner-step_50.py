# === Stage 50: Add unit tests for import and export behavior ===
# Project: CommutePlanner
import unittest
from commute_planner.models import Route, Schedule, Delay, Cost, CommutePlanner
from commute_planner.io import export_routes, export_schedules, export_delays, export_costs

class TestImportExport(unittest.TestCase):
    def test_export_routes(self):
        planner = CommutePlanner()
        planner.add_route(Route("A", "B", 30))
        routes = export_routes(planner)
        self.assertEqual(len(routes), 1)
        self.assertEqual(routes[0].origin, "A")
        self.assertEqual(routes[0].destination, "B")
        self.assertEqual(routes[0].duration, 30)

    def test_export_schedules(self):
        planner = CommutePlanner()
        planner.add_schedule(Schedule("Mon", 7, 9))
        schedules = export_schedules(planner)
        self.assertEqual(len(schedules), 1)
        self.assertEqual(schedules[0].day, "Mon")
        self.assertEqual(schedules[0].start, 7)
        self.assertEqual(schedules[0].end, 9)

    def test_export_delays(self):
        planner = CommutePlanner()
        planner.add_delay(Delay(5, 10))
        delays = export_delays(planner)
        self.assertEqual(len(delays), 1)
        self.assertEqual(delays[0].duration, 5)
        self.assertEqual(delays[0].frequency, 10)

    def test_export_costs(self):
        planner = CommutePlanner()
        planner.add_cost(Cost("Bus", 2.5))
        costs = export_costs(planner)
        self.assertEqual(len(costs), 1)
        self.assertEqual(costs[0].mode, "Bus")
        self.assertEqual(costs[0].price, 2.5)

if __name__ == "__main__":
    unittest.main()
