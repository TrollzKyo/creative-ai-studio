
from pathlib import Path
import argparse

from config.pipelines import VIDEO_PIPELINE

VERSION = "0.0.1"


def show_version():
    print(f"🚀 Creative AI Studio v{VERSION}")


def create_project(name: str):
    base = Path("workspace") / name

    folders = VIDEO_PIPELINE

    base.mkdir(parents=True, exist_ok=True)

    for folder in folders:
        (base / folder).mkdir(exist_ok=True)

    print(f"✅ Project '{name}' created!")
    print(base.resolve())


def list_projects():
    workspace = Path("workspace")

    if not workspace.exists():
        print("Workspace not found.")
        return

    projects = sorted([p for p in workspace.iterdir() if p.is_dir()])

    print(f"\n📁 Projects ({len(projects)})\n")

    if not projects:
        print("No projects found.")
        return

    for index, project in enumerate(projects, start=1):
        print(f"{index}. {project.name}")


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