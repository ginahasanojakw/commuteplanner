# === Stage 32: Add pagination helpers for long console output ===
# Project: CommutePlanner
class Pager:
    def __init__(self, lines_per_page=20):
        self.lines_per_page = lines_per_page
        self.page = 0
        self.total = 0

    def set_content(self, text):
        self.lines = text.splitlines()
        self.total = len(self.lines)
        self.page = 0

    def show_page(self):
        start = self.page * self.lines_per_page
        end = start + self.lines_per_page
        for line in self.lines[start:end]:
            print(line)
        if self.page < self.total - 1:
            print(f"--- Press Enter for next page (page {self.page + 1}/{self.total}) ---")
        input()
        self.page += 1

    def show_all(self):
        for line in self.lines:
            print(line)
        print(f"Done. Total {self.total} lines.")
