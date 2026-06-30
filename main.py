import argparse


VERSION = "0.0.1"


def show_version():
    print(f"🚀 Creative AI Studio v{VERSION}")


def main():
    parser = argparse.ArgumentParser(
        prog="Creative AI Studio",
        description="AI-powered creative workspace",
    )

    parser.add_argument(
        "command",
        nargs="?",
        default="version",
        help="Command to execute",
    )

    args = parser.parse_args()

    if args.command == "version":
        show_version()
    else:
        print(f"Unknown command: {args.command}")


if __name__ == "__main__":
    main()