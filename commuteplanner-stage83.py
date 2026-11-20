# === Stage 83: Add regression tests for the final demo workflow ===
# Project: CommutePlanner
def test_demo_workflow():
    from commute_planner import Route, Schedule, Delay, CostTracker
    route = Route("42", "Home", "Work", 30)
    schedule = Schedule(route, [120, 135, 150])
    delay = Delay(route, 135, 165)
    corrected = schedule.apply_delay(delay)
    assert corrected[1] == 165
    assert corrected[0] == 120
    tracker = CostTracker("Bus", 2.5)
    tracker.log(2)
    assert tracker.total == 5.0
    assert tracker.count == 2
    assert tracker.avg == 2.5
    assert route.estimate(2) == 60
