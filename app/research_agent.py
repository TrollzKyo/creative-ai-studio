from app.base_agent import generate_file


def generate_research(project: str):
    generate_file(
        project=project,
        agent="research",
        input_path="01_Brief/brief.md",
        output_path="02_Research/research.md",
        prompt_file="research",
        success_message="✅ Research Generated",
    )