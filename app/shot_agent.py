from pathlib import Path

from app.ai import ask
from app.router import get_system_prompt


def generate_shotlist(project: str):
    base = Path("workspace") / project

    script_file = base / "03_Script" / "script.md"
    output_file = base / "06_Shoot" / "shotlist.md"

    if not script_file.exists():
        print("❌ Script not found.")
        return

    script = script_file.read_text(encoding="utf-8")

    system = get_system_prompt("video")

    prompt = f"""
Đây là kịch bản video.

Hãy lập Shot List chi tiết.

Mỗi shot gồm:

- Shot số
- Mô tả
- Loại góc máy
- Camera movement
- Lens gợi ý
- Có thể dùng Stock / AI / Hay phải tự quay
- Ghi chú

Script:

{script}
"""

    result = ask(system, prompt)

    output_file.write_text(result, encoding="utf-8")

    print()
    print("✅ Shot List Generated")
    print(output_file.resolve())