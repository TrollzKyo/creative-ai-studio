from app.base_agent import generate_file


def generate_broll(project: str):
    generate_file(
        project=project,
        agent="broll",
        input_path="03_Script/script.md",
        output_path="04_Broll/broll_checklist.md",
        prompt_file="broll",
        success_message="✅ B-roll Checklist Generated",
    )