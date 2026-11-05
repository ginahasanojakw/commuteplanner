# === Stage 57: Add structured result objects for command handlers ===
# Project: CommutePlanner
class CommuteResult:
    def __init__(self, mode, duration, distance, cost):
        self.mode = mode
        self.duration = duration
        self.distance = distance
        self.cost = cost

    def summary(self):
        return (
            f"Mode: {self.mode}, "
            f"Duration: {self.duration} min, "
            f"Distance: {self.distance} km, "
            f"Cost: ${self.cost:.2f}"
        )


class ScheduleResult:
    def __init__(self, departures, arrival_time):
        self.departures = departures
        self.arrival_time = arrival_time

    def summary(self):
        return (
            f"Departures: {self.departures}, "
            f"Arrival: {self.arrival_time}"
        )


class DelayResult:
    def __init__(self, delay_minutes, reason, alternative):
        self.delay_minutes = delay_minutes
        self.reason = reason
        self.alternative = alternative

    def summary(self):
        return (
            f"Delay: {self.delay_minutes} min, "
            f"Reason: {self.reason}, "
            f"Alternative: {self.alternative}"
        )


class CostResult:
    def __init__(self, monthly_pass, per_trip, total_monthly):
        self.monthly_pass = monthly_pass
        self.per_trip = per_trip
        self.total_monthly = total_monthly

    def summary(self):
        return (
            f"Monthly Pass: ${self.monthly_pass:.2f}, "
            f"Per Trip: ${self.per_trip:.2f}, "
            f"Total Monthly: ${self.total_monthly:.2f}"
        )


def plan_commute(result_holder, mode, duration, distance, cost):
    result_holder.mode = mode
    result_holder.duration = duration
    result_holder.distance = distance
    result_holder.cost = cost
    return result_holder


def build_schedule(departures, arrival_time):
    return ScheduleResult(departures, arrival_time)


def build_delay(delay_minutes, reason, alternative):
    return DelayResult(delay_minutes, reason, alternative)


def build_cost(monthly_pass, per_trip, total_monthly):
    return CostResult(monthly_pass, per_trip, total_monthly)


def report(result):
    print(result.summary())
    return result
