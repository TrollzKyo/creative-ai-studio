
import argparse
from app.project import create_project, list_projects


VERSION = "0.0.1"


def show_version():
    print(f"🚀 Creative AI Studio v{VERSION}")



def main():
    parser = argparse.ArgumentParser(
        description="Creative AI Studio"
    )

    sub = parser.add_subparsers(dest="command")

    sub.add_parser("version")
    sub.add_parser("list-projects")

    new_project = sub.add_parser("new-project")
    new_project.add_argument("name")

    args = parser.parse_args()

    if args.command == "version":
        show_version()

    elif args.command == "list-projects":
        list_projects()

    elif args.command == "new-project":
        create_project(args.name)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()