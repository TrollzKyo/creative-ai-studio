from app.script_agent import generate_script
from app.broll_agent import generate_broll
from app.shot_agent import generate_shotlist
from app.premiere_agent import generate_premiere


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

    print("④ Generating Premiere Notes...")
    generate_premiere(project)

    print()
    print("🎉 Project Ready!")