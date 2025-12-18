from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

stream = client.chat.completions.create(
    model="gpt-4o-mini",
    stream=True,
    messages=[
        {"role": "user", "content": "생성형 AI의 개념을 간단히 설명해 주세요."}
    ]
)

for chunk in stream:
    delta = chunk.choices[0].delta
    # delta가 dict가 아니라 ChoiceDelta 객체라서 delta["content"]처럼 대괄호 인덱싱 안 됨.
    content = getattr(delta, "content", None)
    if content:
        print(content, end="", flush=True)
