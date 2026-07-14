import argparse

from app.ai import ask
from app.project import create_project, list_projects
from app.router import get_model, get_system_prompt

from app.script_agent import generate_script
from app.broll_agent import generate_broll
from app.shot_agent import generate_shotlist
from app.premiere_agent import generate_premiere
from app.prepare import prepare

VERSION = "0.0.9"


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

    script = sub.add_parser("script")
    script.add_argument("project")

    broll = sub.add_parser("broll")
    broll.add_argument("project")

    shot = sub.add_parser("shot")
    shot.add_argument("project")

    premiere = sub.add_parser("premiere")
    premiere.add_argument("project")

    prepare_cmd = sub.add_parser("prepare")
    prepare_cmd.add_argument("project")

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
        system = get_system_prompt(args.task)

        print(f"🤖 Using: {model}")
        print()
        print(ask(system, args.prompt))

    elif args.command == "script":
        generate_script(args.project)

    elif args.command == "broll":
        generate_broll(args.project)

    elif args.command == "shot":
        generate_shotlist(args.project)

    elif args.command == "premiere":
        generate_premiere(args.project)

    elif args.command == "prepare":
        prepare(args.project)

    elif args.command == "new-project":
        create_project(args.name)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()