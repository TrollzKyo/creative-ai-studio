import time
from pathlib import Path

from rich.console import Console

from app.ai import ask
from app.router import get_system_prompt
from app.terminal import banner, info, step, done, finish
from config.agents import AGENTS

console = Console()


def generate_file(
    project: str,
    agent: str,
    input_path: str,
    output_path: str,
    prompt_file: str,
    success_message: str,
):
    total_start = time.perf_counter()

    agent_config = AGENTS[agent]

    banner("0.1.1")
    info(project, agent_config["name"])

    base = Path("workspace") / project

    input_file = base / input_path
    output_file = base / output_path

    context_file = base / "14_AI" / "context.md"
    knowledge_file = Path("knowledge") / "company.md"
    prompt_path = Path("prompts") / f"{prompt_file}.md"

    if not input_file.exists():
        console.print(f"[red]❌ Không tìm thấy {input_file}[/red]")
        return

    if not prompt_path.exists():
        console.print(f"[red]❌ Không tìm thấy {prompt_path}[/red]")
        return

    # Read input
    start = time.perf_counter()
    step("Reading input...")
    content = input_file.read_text(encoding="utf-8")
    done(start)

    # Read company knowledge
    knowledge = ""
    if knowledge_file.exists():
        start = time.perf_counter()
        step("Reading company knowledge...")
        knowledge = knowledge_file.read_text(encoding="utf-8")
        done(start)

    # Read project context
    context = ""
    if context_file.exists():
        start = time.perf_counter()
        step("Reading project context...")
        context = context_file.read_text(encoding="utf-8")
        done(start)

    # Read prompt
    start = time.perf_counter()
    step("Loading prompt...")
    prompt_template = prompt_path.read_text(encoding="utf-8")
    done(start)

    # Build prompt
    start = time.perf_counter()
    step("Building prompt...")

    prompt = f"""
========================
COMPANY KNOWLEDGE
========================

{knowledge}

========================
PROJECT CONTEXT
========================

{context}

========================
TASK
========================

{prompt_template.format(content=content)}
"""

    system = get_system_prompt(agent_config["task"])
    done(start)

    # Ask AI
    start = time.perf_counter()

    with console.status(
        "[bold cyan]🤖 GPT-5.5 is thinking...[/bold cyan]",
        spinner="dots",
    ):
        result = ask(system, prompt)

    done(start)

    # Save
    start = time.perf_counter()
    step("Saving output...")
    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(result, encoding="utf-8")
    done(start)

    console.print()
    console.print(f"[bold green]{success_message}[/bold green]")
    console.print(output_file.resolve())

    finish(time.perf_counter() - total_start)