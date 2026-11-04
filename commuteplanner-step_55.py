# === Stage 55: Add a setting to disable colorized output ===
# Project: CommutePlanner
class CommutePlanner:
    def __init__(self):
        self.color_enabled = True

    def print_route(self, route):
        if self.color_enabled:
            print(f"\033[92m{route}\033[0m")
        else:
            print(route)

    def print_delay(self, delay):
        if self.color_enabled:
            print(f"\033[91m{delay}\033[0m")
        else:
            print(delay)

    def print_cost(self, cost):
        if self.color_enabled:
            print(f"\033[93m{cost}\033[0m")
        else:
            print(cost)

    def print_schedule(self, schedule):
        if self.color_enabled:
            print(f"\033[94m{schedule}\033[0m")
        else:
            print(schedule)

    def set_color_disabled(self):
        self.color_enabled = False

    def set_color_enabled(self):
        self.color_enabled = True

    def toggle_color(self):
        self.color_enabled = not self.color_enabled

    def format_route(self, route):
        if self.color_enabled:
            return f"\033[92m{route}\033[0m"
        return route

    def format_delay(self, delay):
        if self.color_enabled:
            return f"\033[91m{delay}\033[0m"
        return delay

    def format_cost(self, cost):
        if self.color_enabled:
            return f"\033[93m{cost}\033[0m"
        return cost

    def format_schedule(self, schedule):
        if self.color_enabled:
            return f"\033[94m{schedule}\033[0m"
        return schedule
