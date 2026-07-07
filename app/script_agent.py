from pathlib import Path

from app.ai import ask
from app.router import get_system_prompt


def generate_script(project: str):
    base = Path("workspace") / project

    brief_file = base / "01_Brief" / "brief.md"
    output_file = base / "03_Script" / "script.md"

    if not brief_file.exists():
        print("❌ Không tìm thấy:")
        print(brief_file)
        return

    brief = brief_file.read_text(encoding="utf-8")

    system = get_system_prompt("video")

    prompt = f"""
Bạn hãy viết một kịch bản video chuyên nghiệp dựa trên brief sau.

Yêu cầu:

- Có tiêu đề
- Mục tiêu video
- Chia thành từng cảnh
- Voice Over
- Gợi ý B-roll
- Thời lượng từng cảnh

Brief:

{brief}
"""

    result = ask(system, prompt)

    output_file.write_text(result, encoding="utf-8")

    print("✅ Script generated!")
    print(output_file.resolve())