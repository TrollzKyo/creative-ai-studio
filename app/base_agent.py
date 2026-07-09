import time
from pathlib import Path

from rich.console import Console
from rich.status import Status

from app.ai import ask
from app.router import get_system_prompt
from app.terminal import banner, info, step, done, finish

console = Console()


def generate_file(
    project: str,
    input_path: str,
    output_path: str,
    task: str,
    prompt_template: str,
    success_message: str,
):
    total_start = time.perf_counter()

    banner("0.0.6")
    info(project, task)

    base = Path("workspace") / project

    input_file = base / input_path
    output_file = base / output_path

    if not input_file.exists():
        console.print(f"[red]❌ Không tìm thấy {input_file}[/red]")
        return

    start = time.perf_counter()
    step("Reading input...")
    content = input_file.read_text(encoding="utf-8")
    done(start)

    start = time.perf_counter()
    step("Building prompt...")
    system = get_system_prompt(task)
    prompt = prompt_template.format(content=content)
    done(start)

    start = time.perf_counter()

    with console.status(
        "[bold cyan]🤖 GPT-5.5 is thinking...[/bold cyan]",
        spinner="dots",
    ):
        result = ask(system, prompt)

    done(start)

    start = time.perf_counter()
    step("Saving output...")
    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(result, encoding="utf-8")
    done(start)

    console.print()
    console.print(f"[bold green]{success_message}[/bold green]")
    console.print(output_file.resolve())

    finish(time.perf_counter() - total_start)