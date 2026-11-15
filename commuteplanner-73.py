# === Stage 73: Add a lightweight HTML report export ===
# Project: CommutePlanner
def export_html_report(data, filename="commute_report.html"):
    routes = data.get("routes", [])
    total_cost = sum(r.get("total_cost", 0) for r in routes)
    total_time = sum(r.get("avg_time", 0) for r in routes)
    lines = ["<!DOCTYPE html>", "<html><head><meta charset='utf-8'>", "<title>CommutePlanner Report</title>", "<style>body{font-family:sans-serif;max-width:800px;margin:20px auto}table{border-collapse:collapse}td,th{border:1px solid #ccc;padding:8px;text-align:left}</style>", "</head><body>", "<h1>Commute Report</h1>", f"<p>Total Cost: ${total_cost}</p>", f"<p>Total Time: {total_time} minutes</p>"]
    lines.append("<table><tr><th>Route</th><th>Duration</th><th>Cost</th></tr>")
    for r in routes:
        lines.append(f"<tr><td>{r.get('name','')}</td><td>{r.get('avg_time','')} min</td><td>${r.get('total_cost','')}</td></tr>")
    lines.append("</table>")
    lines.append("</body></html>")
    with open(filename, "w") as f:
        f.write("\n".join(lines))
    return filename
