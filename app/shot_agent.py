from app.base_agent import generate_file


def generate_shotlist(project: str):
    generate_file(
        project=project,
        agent="shot",
        input_path="03_Script/script.md",
        output_path="06_Shoot/shotlist.md",
        prompt_template="""
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

{content}
""",
        success_message="✅ Shot List Generated",
    )