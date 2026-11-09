# === Stage 61: Add performance timing for core list and search operations ===
# Project: CommutePlanner
import time

def time_operation(func, *args, **kwargs):
    start = time.perf_counter()
    result = func(*args, **kwargs)
    elapsed = time.perf_counter() - start
    return result, elapsed

class TimingCollector:
    def __init__(self):
        self.operations = {}

    def run(self, name, func, *args, **kwargs):
        result, elapsed = time_operation(func, *args, **kwargs)
        self.operations[name] = self.operations.get(name, 0) + 1
        self.operations[name + "_time"] = self.operations.get(name + "_time", 0) + elapsed
        return result

    def report(self):
        for name, count in self.operations.items():
            if name.endswith("_time"):
                continue
            total = self.operations[name + "_time"]
            print(f"{name}: {count} runs, {total:.6f}s total, {total / count:.6f}s avg")

def benchmark_search(routes, query):
    collector = TimingCollector()
    results = []
    for route in routes:
        if query in route["name"]:
            results.append(route)
    collector.run("search", lambda: results, routes, query)
    return results

def benchmark_contains(lst, item):
    collector = TimingCollector()
    result = item in lst
    collector.run("contains", lambda: result, lst, item)
    return result

def benchmark_append(lst, item):
    collector = TimingCollector()
    lst.append(item)
    collector.run("append", lambda: None, lst, item)
    return lst

def benchmark_sort(routes, key):
    collector = TimingCollector()
    sorted_routes = sorted(routes, key=key)
    collector.run("sort", lambda: sorted_routes, routes, key)
    return sorted_routes
