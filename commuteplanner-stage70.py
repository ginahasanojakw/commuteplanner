# === Stage 70: Add a clear-state command protected by a confirmation flag ===
# Project: CommutePlanner
CLEAR_CONFIRM = {"flag": False, "token": None}

def cmd_clear_state(args):
    if not CLEAR_CONFIRM["flag"]:
        print("A confirmation is required before clearing state.")
        return
    if CLEAR_CONFIRM["token"] != args.get("token"):
        print("Incorrect confirmation token. State not cleared.")
        return
    CLEAR_CONFIRM["flag"] = False
    CLEAR_CONFIRM["token"] = None
    print("State cleared.")

def cmd_clear_confirm(args):
    CLEAR_CONFIRM["flag"] = True
    CLEAR_CONFIRM["token"] = args.get("token")
    print("Confirmation requested. Use a token to proceed.")
