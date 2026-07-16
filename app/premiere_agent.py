from app.base_agent import generate_file


def generate_premiere(project: str):
    generate_file(
        project=project,
        agent="premiere",
        input_path="06_Shoot/shotlist.md",
        output_path="07_Premiere/edit_notes.md",
        prompt_file="premiere",
        success_message="✅ Premiere Edit Notes Generated",
    )