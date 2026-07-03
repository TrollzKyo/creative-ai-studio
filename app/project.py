

from pathlib import Path

from config.video_pipeline import VIDEO_PIPELINE

def create_ai_files(base: Path):
    ai = base / "14_AI"

    (ai / "prompts.md").write_text(
"""# Prompts

## ChatGPT

## Kling

## Midjourney

## Suno
""",
        encoding="utf-8",
    )

    (ai / "references.md").write_text(
"""# References

-
""",
        encoding="utf-8",
    )

    (ai / "notes.md").write_text(
"""# Notes

-
""",
        encoding="utf-8",
    )


def create_project(name: str):
    base = Path("workspace") / name

    folders = VIDEO_PIPELINE

    base.mkdir(parents=True, exist_ok=True)

    for folder in folders:
        (base / folder).mkdir(exist_ok=True)

    create_ai_files(base)

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