# === Stage 76: Add graceful keyboard interrupt handling in the CLI entry point ===
# Project: CommutePlanner
try:
    main()
except KeyboardInterrupt:
    print()
    print("CommutePlanner stopped. Goodbye.")
    sys.exit(0)
