from pathlib import Path

from app.ai import ask
from app.router import get_system_prompt


def generate_script(project: str):
    base = Path("workspace") / project

    brief_file = base / "01_Brief" / "brief.md"
    output_file = base / "03_Script" / "script.md"

    if not brief_file.exists():
        print("❌ Brief not found.")
        return

    brief = brief_file.read_text(encoding="utf-8")

    system = get_system_prompt("video")

    prompt = f"""
Dựa trên brief sau đây hãy viết một kịch bản video hoàn chỉnh.

Yêu cầu:

- Tiêu đề
- Mục tiêu
- Insight
- Big Idea
- Storyline
- Bảng kịch bản

Brief:

{brief}
"""

    result = ask(system, prompt)

    output_file.write_text(result, encoding="utf-8")

    print()
    print("✅ Script Generated")
    print(output_file.resolve())