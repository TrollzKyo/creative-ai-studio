from pathlib import Path

from app.research_agent import generate_research
from app.script_agent import generate_script
from app.broll_agent import generate_broll
from app.shot_agent import generate_shotlist
from app.assets_agent import generate_assets
from app.premiere_agent import generate_premiere
from app.status import show_status


def run_project(project: str):
    root = Path("workspace") / project

    print()
    print(f"🚀 Running Project: {project}")
    print()

    if not (root / "02_Research/research.md").exists():
        generate_research(project)
    else:
        print("⏩ Research already exists")

    if not (root / "03_Script/script.md").exists():
        generate_script(project)
    else:
        print("⏩ Script already exists")

    if not (root / "04_Broll/broll_checklist.md").exists():
        generate_broll(project)
    else:
        print("⏩ B-roll already exists")

    if not (root / "06_Shoot/shotlist.md").exists():
        generate_shotlist(project)
    else:
        print("⏩ Shot List already exists")

    if not (root / "07_Premiere/assets.md").exists():
        generate_assets(project)
    else:
        print("⏩ Assets already exist")

    if not (root / "07_Premiere/edit_notes.md").exists():
        generate_premiere(project)
    else:
        print("⏩ Premiere Notes already exist")

    print()
    show_status(project)