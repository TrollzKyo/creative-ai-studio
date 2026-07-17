from app.base_agent import generate_file


def generate_subtitle(project: str):
    generate_file(
        project=project,
        agent="premiere",
        input_path="03_Script/script.md",
        output_path="07_Premiere/subtitle.srt",
        prompt_file="subtitle",
        success_message="✅ Subtitle Generated",
    )