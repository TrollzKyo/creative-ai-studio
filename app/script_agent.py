from app.base_agent import generate_file


def generate_script(project: str):
    generate_file(
        project=project,
        agent="script",
        input_path="01_Brief/brief.md",
        output_path="03_Script/script.md",
        prompt_file="script",
        success_message="✅ Script Generated",
    )