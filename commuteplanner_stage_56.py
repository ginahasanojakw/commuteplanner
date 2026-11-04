# === Stage 56: Add compact error classes for domain failures ===
# Project: CommutePlanner
class CommuteError(Exception):
    pass

class RouteNotFoundError(CommuteError):
    pass

class ScheduleNotFoundError(CommuteError):
    pass

class DelayExceedsThresholdError(CommuteError):
    pass

class CostExceedsBudgetError(CommuteError):
    pass

class InvalidTimeError(CommuteError):
    pass

class InvalidCostError(CommuteError):
    pass

class NoAvailableRouteError(CommuteError):
    pass

class InsufficientFundsError(CommuteError):
    pass

class RouteValidationError(CommuteError):
    pass

class ScheduleValidationError(CommuteError):
    pass

class DelayAnomalyError(CommuteError):
    pass

class InsufficientDataError(CommuteError):
    pass

class InvalidStopError(CommuteError):
    pass

class RouteOverlapError(CommuteError):
    pass

class ScheduleConflictError(CommuteError):
    pass

class CostCalculationError(CommuteError):
    pass

class PlannerStateError(CommuteError):
    pass

class RouteScheduleMismatchError(CommuteError):
    pass

class DelayPatternError(CommuteError):
    pass

class BudgetExceededError(CommuteError):
    pass
