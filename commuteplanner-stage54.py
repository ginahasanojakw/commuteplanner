# === Stage 54: Add colorized output through optional ANSI codes ===
# Project: CommutePlanner
def colorize(text, color):
    codes = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'magenta': '\033[95m',
        'cyan': '\033[96m',
        'white': '\033[97m',
        'gray': '\033[90m',
        'bold': '\033[1m',
        'dim': '\033[2m',
        'reset': '\033[0m',
    }
    return f"{codes.get(color, '')}{text}{codes.get('reset', '')}"

def use_color():
    return os.environ.get('NO_COLOR') is None and sys.stdout.isatty()

def print_route(route):
    name = route.get('name', 'Route')
    print(colorize(f"Route: {name}", 'bold'))
    for stop in route.get('stops', []):
        print(f"  {stop}")
    print()

def print_schedule(schedule):
    print(colorize("Schedule:", 'cyan'))
    for dep in schedule.get('departures', []):
        delay = dep.get('delay')
        if delay:
            print(colorize(f"{dep['time']} -> {dep['destination']} ({delay} min delay)", 'yellow'))
        else:
            print(f"  {dep['time']} -> {dep['destination']}")
    print()

def print_cost(costs):
    print(colorize("Cost Summary:", 'green'))
    for key, value in costs.items():
        print(f"  {key}: {value}")
    print()
