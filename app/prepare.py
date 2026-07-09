from app.script_agent import generate_script
from app.broll_agent import generate_broll
from app.shot_agent import generate_shotlist


def prepare(project: str):
    print()
    print("🚀 Preparing Project")
    print()

    print("① Generating Script...")
    generate_script(project)

    print()

    print("② Generating B-roll...")
    generate_broll(project)

    print()

    print("③ Generating Shot List...")
    generate_shotlist(project)

    print()
    print("🎉 Project Ready!")