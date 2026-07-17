from app.base_agent import generate_file


def generate_memory(project: str):
    generate_file(
        project=project,
        agent="premiere",
        input_path="14_AI/context.md",
        output_path="14_AI/memory.md",
        prompt_file="memory",
        success_message="✅ Project Memory Generated",
    )