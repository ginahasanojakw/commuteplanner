# === Stage 49: Add unit tests for update and delete edge cases ===
# Project: CommutePlanner
class TestCommutePlannerEdgeCases:
    def test_update_nonexistent_route(self):
        planner = CommutePlanner()
        planner.add_route("A", "B", 30)
        with pytest.raises(KeyError):
            planner.update_route("A", "B", 40, "C")

    def test_delete_nonexistent_route(self):
        planner = CommutePlanner()
        planner.add_route("A", "B", 30)
        with pytest.raises(KeyError):
            planner.delete_route("A", "B", "C")

    def test_update_same_route(self):
        planner = CommutePlanner()
        planner.add_route("A", "B", 30)
        planner.update_route("A", "B", 35, "C")
        assert planner.get_route("A", "B") == 35

    def test_delete_only_route(self):
        planner = CommutePlanner()
        planner.add_route("A", "B", 30)
        planner.delete_route("A", "B", "C")
        assert len(planner.routes) == 0
