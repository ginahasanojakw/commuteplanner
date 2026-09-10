# === Stage 16: Add argparse support for the most common commands ===
# Project: CommutePlanner
import argparse

def main():
    parser = argparse.ArgumentParser(description="CommutePlanner CLI")
    sub = parser.add_subparsers(dest="command")

    p_route = sub.add_parser("route", help="Plan a route")
    p_route.add_argument("--from", help="Origin")
    p_route.add_argument("--to", help="Destination")
    p_route.add_argument("--mode", choices=["walk", "bike", "bus", "train", "car"], default="bus")

    p_schedule = sub.add_parser("schedule", help="Show schedule")
    p_schedule.add_argument("--line", help="Transport line")
    p_schedule.add_argument("--date", help="Date (YYYY-MM-DD)")

    p_cost = sub.add_parser("cost", help="Calculate cost")
    p_cost.add_argument("--route", help="Route file")
    p_cost.add_argument("--trips", type=int, default=1)

    p_delay = sub.add_parser("delay", help="Report delays")
    p_delay.add_argument("--line", help="Transport line")
    p_delay.add_argument("--days", type=int, default=7)

    args = parser.parse_args()
    if args.command is None:
        parser.print_help()
        return
    print(f"[{args.command}] -- {getattr(args, 'from', '')} -> {getattr(args, 'to', '')}")

if __name__ == "__main__":
    main()
