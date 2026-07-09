import time

from rich.console import Console
from rich.panel import Panel

console = Console()


def banner(version: str):
    console.print(
        Panel.fit(
            f"[bold cyan]🚀 Creative AI Studio[/bold cyan]\nVersion {version}",
            border_style="cyan",
        )
    )


def info(project: str, agent: str):
    console.print(f"[cyan]📂 Project[/cyan] : {project}")
    console.print(f"[cyan]🤖 Agent[/cyan]   : {agent}")
    console.print("[cyan]🧠 Model[/cyan]   : GPT-5.5")
    console.rule()


def step(text: str):
    console.print(f"[yellow]▶[/yellow] {text}")


def done(start: float):
    elapsed = time.perf_counter() - start
    console.print(f"[green]✔ Done[/green] ({elapsed:.2f}s)")


def finish(total: float):
    console.rule()
    console.print(
        f"[bold green]🎉 Finished[/bold green] in [cyan]{total:.2f}s[/cyan]"
    )