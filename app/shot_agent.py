from app.base_agent import generate_file


def generate_shotlist(project: str):
    generate_file(
        project=project,
        agent="shot",
        input_path="03_Script/script.md",
        output_path="06_Shoot/shotlist.md",
        prompt_file="shot",
        success_message="✅ Shot List Generated",
    )