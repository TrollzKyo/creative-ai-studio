from app.base_agent import generate_file


def generate_assets(project: str):
    generate_file(
        project=project,
        agent="premiere",
        input_path="06_Shoot/shotlist.md",
        output_path="07_Premiere/assets.md",
        prompt_file="assets",
        success_message="✅ Asset Planner Generated",
    )