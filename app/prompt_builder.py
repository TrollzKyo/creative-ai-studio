from pathlib import Path
import json


def build_prompt(project, prompt_file, content):

    base = Path("workspace") / project

    knowledge = ""
    context = ""
    manifest = ""

    knowledge_file = Path("knowledge/company.md")
    context_file = base / "14_AI/context.md"
    manifest_file = base / "project.json"
    prompt_path = Path("prompts") / f"{prompt_file}.md"

    if knowledge_file.exists():
        knowledge = knowledge_file.read_text(encoding="utf-8")

    if context_file.exists():
        context = context_file.read_text(encoding="utf-8")

    if manifest_file.exists():
        manifest = json.dumps(
            json.loads(
                manifest_file.read_text(encoding="utf-8")
            ),
            indent=2,
            ensure_ascii=False,
        )

    prompt = prompt_path.read_text(encoding="utf-8")

    return f"""
==========================
COMPANY KNOWLEDGE
==========================

{knowledge}

==========================
PROJECT MANIFEST
==========================

{manifest}

==========================
PROJECT CONTEXT
==========================

{context}

==========================
TASK
==========================

{prompt.format(content=content)}
"""