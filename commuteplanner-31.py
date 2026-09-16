# === Stage 31: Add compact table rendering for long lists ===
# Project: CommutePlanner
class CompactTable:
    def __init__(self, headers, data):
        self.headers = headers
        self.data = data

    def render(self):
        col_widths = [len(h) for h in self.headers]
        for row in self.data:
            for i, cell in enumerate(row):
                col_widths[i] = max(col_widths[i], len(str(cell)))
        lines = [self._format_line(self.headers, col_widths)]
        for row in self.data:
            lines.append(self._format_line(row, col_widths))
        return "\n".join(lines)

    def _format_line(self, items, widths):
        return " | ".join(str(item).ljust(widths[i]) for i, item in enumerate(items))
