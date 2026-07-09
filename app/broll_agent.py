from app.base_agent import generate_file


def generate_broll(project: str):
    generate_file(
        project=project,
        agent="broll",
        input_path="03_Script/script.md",
        output_path="04_Broll/broll_checklist.md",
        prompt_template="""
Đây là kịch bản video.

Hãy phân tích và tạo Checklist B-roll.

Với mỗi cảnh hãy ghi:

- Mô tả cảnh
- Cần B-roll gì
- Keyword tiếng Anh để tìm trên Pexels / Artgrid / Envato
- Có thể dùng Stock / AI / Hay phải tự quay
- Ghi chú

Script:

{content}
""",
        success_message="✅ B-roll Checklist Generated",
    )