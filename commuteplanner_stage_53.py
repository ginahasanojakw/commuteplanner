# === Stage 53: Add command help text and usage examples ===
# Project: CommutePlanner
def print_help():
    help_text = (
        "CommutePlanner - plan and track your daily commute.\n"
        "\n"
        "Usage:\n"
        "  python commute.py <command> [options]\n"
        "\n"
        "Commands:\n"
        "  add-route     Add a new commute route\n"
        "  add-schedule  Add a departure schedule to a route\n"
        "  add-delay     Record a delay for a scheduled departure\n"
        "  add-cost      Log travel cost for a route\n"
        "  show-routes   List all known routes\n"
        "  show-schedule Show the schedule for a route\n"
        "  show-costs    Show cost history for a route\n"
        "  help          Show this help message\n"
        "\n"
        "Examples:\n"
        "  python commute.py show-routes\n"
        "  python commute.py add-schedule home-to-work 07:30\n"
        "  python commute.py add-delay home-to-work 07:30 15\n"
        "  python commute.py add-cost home-to-work 4.50\n"
    )
    print(help_text)
