from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()


def ask(system_prompt: str, prompt: str):
    response = client.responses.create(
        model="gpt-5.5",
        input=[
            {
                "role": "system",
                "content": (
                    system_prompt
                    + "\n\n"
                    + "Bạn là trợ lý AI của Creative AI Studio. "
                    + "Luôn trả lời bằng tiếng Việt, trừ khi người dùng yêu cầu ngôn ngữ khác. "
                    + "Trả lời ngắn gọn, rõ ràng, thực tế."
                ),
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
    )

    return response.output_text