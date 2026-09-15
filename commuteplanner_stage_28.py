# === Stage 28: Add overdue item detection based on due dates ===
# Project: CommutePlanner
def detect_overdue(self):
        today = datetime.date.today()
        overdue = []
        for entry in self.entries:
            if entry.is_overdue:
                overdue.append(entry)
        return overdue
