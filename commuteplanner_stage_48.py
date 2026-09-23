# === Stage 48: Add small unit tests for creation and validation helpers ===
# Project: CommutePlanner
import pytest

from commute_planner.models import Route, Schedule, Delay, Cost, RouteSchedule
from commute_planner.helpers import create_route, create_schedule, create_delay, create_cost, validate_route, validate_schedule, validate_cost


def test_create_route():
    route = create_route(name="Main St", distance=5.0, duration=15)
    assert route.name == "Main St"
    assert route.distance == 5.0
    assert route.duration == 15


def test_create_schedule():
    sched = create_schedule(route_id=1, departure=600, arrival=615)
    assert sched.route_id == 1
    assert sched.departure == 600
    assert sched.arrival == 615


def test_create_delay():
    delay = create_delay(route_id=1, minutes=5)
    assert delay.route_id == 1
    assert delay.minutes == 5


def test_create_cost():
    cost = create_cost(route_id=1, currency="USD", amount=1.5)
    assert cost.route_id == 1
    assert cost.currency == "USD"
    assert cost.amount == 1.5


def test_validate_route():
    r = Route(name="Test", distance=3.0, duration=10)
    assert validate_route(r) is True


def test_validate_schedule():
    s = Schedule(route_id=1, departure=600, arrival=615)
    assert validate_schedule(s) is True


def test_validate_delay():
    d = Delay(route_id=1, minutes=3)
    assert validate_delay(d) is True


def test_validate_cost():
    c = Cost(route_id=1, currency="USD", amount=2.0)
    assert validate_cost(c) is True


def test_route_schedule_creation():
    rs = RouteSchedule(route=Route(name="A", distance=2.0, duration=5),
                       schedule=Schedule(route_id=1, departure=600, arrival=605))
    assert rs.route.name == "A"
    assert rs.schedule.departure == 600
