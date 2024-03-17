import requests
from env import env


def chat_completion(messageList: list):
    response = requests.post(
        url="https://api.openai.com/v1/chat/completions",
        headers={"Authorization": f"Bearer {env.OPENAI_API_KEY}"},
        json={
            "model": "gpt-4",
            "messages": messageList,
            "temperature": 0,
        },
        proxies=(
            {
                "http": "http://krmp-proxy.9rum.cc:3128",
                "https": "http://krmp-proxy.9rum.cc:3128",
            }
            if env.isProduction
            else None
        ),
    )

    chat_completion_object = response.json()
    result = chat_completion_object["choices"][0]["message"]["content"]
    return result
