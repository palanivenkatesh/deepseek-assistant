import os
from openai import OpenAI
import replicate
from playsound import playsound

api_key = os.environ.get("DEEPSEEK_API_KEY")
client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")

SYSTEM_PROMPT = "You are a helpful assistant"


def chat():
    history = []
    history.append({"role": "system", "content": SYSTEM_PROMPT})
    while True:
        user_input = input("You: ")
        history.append({"role": "user", "content": user_input})
        response = client.chat.completions.create(
            model="deepseek-reasoner",
            messages=history,
            stream=False,
        )

        answer = response.choices[0].message.content
        history.append({"role": "assistant", "content": answer})
        print(answer)
        say(answer)


def say(text):
    input = {
        "text": text,
        "speed": 1.1,
        "voice": "af_bella",
    }

    output = replicate.run(
        "jaaari/kokoro-82m:dfdf537ba482b029e0a761699e6f55e9162cfd159270bfe0e44857caa5f275a6",
        input=input,
    )
    with open("output.wav", "wb") as file:
        file.write(output.read())
    playsound("output.wav")
    # => output.wav written to disk


chat()
