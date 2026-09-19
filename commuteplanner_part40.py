# === Stage 40: Add plain text report export ===
# Project: CommutePlanner
def export_text_report(self, filename):
    """Export trip data to a plain text report."""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("CommutePlanner Report\n")
        f.write("=" * 40 + "\n\n")
        if self.routes:
            f.write("Routes:\n")
            for route in self.routes:
                f.write(f"  {route}\n")
            f.write("\n")
        if self.schedules:
            f.write("Schedules:\n")
            for sched in self.schedules:
                f.write(f"  {sched}\n")
            f.write("\n")
        if self.delays:
            f.write("Delays:\n")
            for delay in self.delays:
                f.write(f"  {delay}\n")
            f.write("\n")
        if self.costs:
            f.write("Costs:\n")
            for cost in self.costs:
                f.write(f"  {cost}\n")
            f.write("\n")
        f.write(f"Total routes: {len(self.routes)}\n")
        f.write(f"Total schedules: {len(self.schedules)}\n")
        f.write(f"Total delays: {len(self.delays)}\n")
        f.write(f"Total costs: {len(self.costs)}\n")
