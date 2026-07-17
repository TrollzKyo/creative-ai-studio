from pathlib import Path


CHECKS = [
    ("Research", "02_Research/research.md"),
    ("Script", "03_Script/script.md"),
    ("B-roll", "04_Broll/broll_checklist.md"),
    ("Shot List", "06_Shoot/shotlist.md"),
    ("Asset Planner", "07_Premiere/assets.md"),
    ("Premiere Notes", "07_Premiere/edit_notes.md"),
]


def show_status(project: str):
    root = Path("workspace") / project

    print()
    print(f"📂 Project : {project}")
    print()

    done = 0

    for name, file in CHECKS:
        if (root / file).exists():
            print(f"✅ {name}")
            done += 1
        else:
            print(f"❌ {name}")

    print()

    percent = int(done / len(CHECKS) * 100)
    print(f"Progress : {percent}%")