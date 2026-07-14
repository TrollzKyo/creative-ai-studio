from app.base_agent import generate_file


def generate_premiere(project: str):
    generate_file(
        project=project,
        agent="premiere",
        input_path="06_Shoot/shotlist.md",
        output_path="07_Premiere/edit_notes.md",
        prompt_template="""
Bạn là Senior Video Editor.

Dựa trên Shot List hãy tạo hướng dẫn dựng trong Premiere.

Bao gồm:

# Timeline

- Intro
- Main
- Ending

# Transition

- Cảnh nào nên cut
- Cảnh nào fade
- Cảnh nào whip
- Cảnh nào zoom

# Motion

- Scale
- Position
- Speed Ramp

# Text

- Lower Third
- Caption
- CTA

# Color

- Tone

# Ghi chú cho Editor

Shot List:

{content}
""",
        success_message="✅ Premiere Edit Notes Generated",
    )