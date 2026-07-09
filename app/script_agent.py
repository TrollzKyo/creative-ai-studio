from app.base_agent import generate_file


def generate_script(project: str):
    generate_file(
        project=project,
        agent="script",
        input_path="01_Brief/brief.md",
        output_path="03_Script/script.md",
        prompt_template="""
Dựa trên brief sau đây hãy viết một kịch bản video hoàn chỉnh.

Yêu cầu:

- Tiêu đề
- Mục tiêu
- Insight
- Big Idea
- Storyline
- Bảng kịch bản

Brief:

{content}
""",
        success_message="✅ Script Generated",
    )