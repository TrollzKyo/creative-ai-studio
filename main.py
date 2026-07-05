import argparse

from app.ai import ask
from app.project import create_project, list_projects
from app.router import get_model, get_system_prompt

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
    sub.add_parser("models")

    chat = sub.add_parser("ask")
    chat.add_argument("task")
    chat.add_argument("prompt")

    new_project = sub.add_parser("new-project")
    new_project.add_argument("name")

    args = parser.parse_args()

    if args.command == "version":
        show_version()

    elif args.command == "list-projects":
        list_projects()

    elif args.command == "models":
        for task in [
            "video",
            "design",
            "document",
            "code",
            "unity",
            "unreal",
        ]:
            print(f"{task:<10} -> {get_model(task)}")

    elif args.command == "ask":
        model = get_model(args.task)
        system_prompt = get_system_prompt(args.task)

        print(f"🤖 Using: {model}")
        print()

        print(ask(system_prompt, args.prompt))

    elif args.command == "new-project":
        create_project(args.name)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()