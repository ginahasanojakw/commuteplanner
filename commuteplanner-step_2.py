# === Stage 2: Add dataclasses or typed dictionaries for the main domain records ===
# Project: CommutePlanner
from dataclasses import dataclass
from datetime import datetime, timedelta

@dataclass
class Stop:
    name: str
    coordinates: tuple[float, float]
    transfers: list["Stop"] = None

@dataclass
class Schedule:
    stop_name: str
    date_time: datetime
    delay_minutes: float = 0.0

@dataclass
class Cost:
    route_name: str
    amount: float
    currency: str = "USD"
    timestamp: datetime = None

@dataclass
class Route:
    name: str
    stops: list[Stop]
    schedule: list[Schedule]
    costs: list[Cost]
