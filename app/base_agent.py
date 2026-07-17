import time
from pathlib import Path

from rich.console import Console

from app.ai import ask
from app.prompt_builder import build_prompt
from app.router import get_system_prompt
from app.terminal import banner, info, step, done, finish
from app.logger import log
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

    banner("0.1.7")
    info(project, agent_config["name"])

    log(f"START | {agent} | {project}")

    base = Path("workspace") / project

    input_file = base / input_path
    output_file = base / output_path
    memory_file = base / "14_AI" / "memory.md"

    if not input_file.exists():
        console.print(f"[red]❌ Không tìm thấy {input_file}[/red]")
        log(f"ERROR | Missing input: {input_file}")
        return

    # Read input
    start = time.perf_counter()
    step("Reading input...")

    content = input_file.read_text(encoding="utf-8")

    done(start)

    # Build Prompt
    start = time.perf_counter()
    step("Building prompt...")

    prompt = build_prompt(
        project=project,
        prompt_file=prompt_file,
        content=content,
    )

    # Inject Project Memory
    if memory_file.exists():
        memory = memory_file.read_text(encoding="utf-8")

        prompt = f"""
# PROJECT MEMORY

{memory}

---

{prompt}
"""

    system = get_system_prompt(agent_config["task"])

    done(start)

    # GPT
    start = time.perf_counter()

    try:
        with console.status(
            "[bold cyan]🤖 GPT-5.5 is thinking...[/bold cyan]",
            spinner="dots",
        ):
            result = ask(system, prompt)

        done(start)

    except Exception as e:
        console.print(f"[red]❌ {e}[/red]")
        log(f"ERROR | {agent} | {e}")
        return

    # Save
    start = time.perf_counter()
    step("Saving output...")

    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(result, encoding="utf-8")

    done(start)

    console.print()
    console.print(f"[bold green]{success_message}[/bold green]")
    console.print(output_file.resolve())

    elapsed = time.perf_counter() - total_start

    log(f"SUCCESS | {agent} | {project} | {elapsed:.2f}s")

    finish(elapsed)