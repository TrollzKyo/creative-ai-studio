from app.research_agent import generate_research
from app.script_agent import generate_script
from app.broll_agent import generate_broll
from app.shot_agent import generate_shotlist
from app.premiere_agent import generate_premiere


def prepare(project: str):
    print()
    print("🚀 Preparing Project")
    print()

    print("① Research...")
    generate_research(project)

    print()

    print("② Script...")
    generate_script(project)

    print()

    print("③ B-roll...")
    generate_broll(project)

    print()

    print("④ Shot List...")
    generate_shotlist(project)

    print()

    print("⑤ Premiere Notes...")
    generate_premiere(project)

    print()
    print("🎉 Project Ready!")