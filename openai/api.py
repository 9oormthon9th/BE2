import time
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


def assistant_create_thread():
    response = requests.post(
        url="https://api.openai.com/v1/threads",
        headers={
            "Authorization": f"Bearer {env.OPENAI_API_KEY}",
            "Content-Type": "application/json",
            "OpenAI-Beta": "assistants=v1",
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

    thread_object = response.json()
    result = thread_object["id"]
    return result


def assistant_create_message(thread_id, message):
    response = requests.post(
        url=f"https://api.openai.com/v1/threads/{thread_id}/messages",
        headers={
            "Authorization": f"Bearer {env.OPENAI_API_KEY}",
            "Content-Type": "application/json",
            "OpenAI-Beta": "assistants=v1",
        },
        json={"role": "user", "content": message},
        proxies=(
            {
                "http": "http://krmp-proxy.9rum.cc:3128",
                "https": "http://krmp-proxy.9rum.cc:3128",
            }
            if env.isProduction
            else None
        ),
    )

    message_object = response.json()
    print(message_object)


def assistant_create_thread_and_run(user_input: str):
    response = requests.post(
        url=f"https://api.openai.com/v1/threads/runs",
        headers={
            "Authorization": f"Bearer {env.OPENAI_API_KEY}",
            "Content-Type": "application/json",
            "OpenAI-Beta": "assistants=v1",
        },
        json={
            "assistant_id": "asst_L0nzOovwv494euGuAR87mSIO",
            "thread": {"messages": [{"role": "user", "content": user_input}]},
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

    run_object = response.json()
    return run_object["thread_id"], run_object["id"]


def assistant_retrieve_run(thread_id: str, run_id: str):
    response = requests.get(
        url=f"https://api.openai.com/v1/threads/{thread_id}/runs/{run_id}",
        headers={
            "Authorization": f"Bearer {env.OPENAI_API_KEY}",
            "Content-Type": "application/json",
            "OpenAI-Beta": "assistants=v1",
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

    run_object = response.json()
    return run_object


def assistant_wait_for_run(thread_id: str, run_id: str):
    while True:
        # 작업의 상태 확인
        run_object = assistant_retrieve_run(thread_id, run_id)
        status = run_object["status"]

        if status == "completed":
            return run_object
        elif status == "failed":
            # TODO: 다른 status도 처리하기
            print("작업이 실패했습니다.")
            break
        else:
            time.sleep(1)


def assistant_list_message(thread_id: str):
    response = requests.get(
        url=f"https://api.openai.com/v1/threads/{thread_id}/messages",
        headers={
            "Authorization": f"Bearer {env.OPENAI_API_KEY}",
            "Content-Type": "application/json",
            "OpenAI-Beta": "assistants=v1",
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

    message_object_list = response.json()
    return message_object_list["data"]


def course_recommend_pipeline(user_input: str):
    """Ask gpt for recommendation, wait, then return answer parsed
    :return: courseCode
    :rtype: str
    """
    thread_id, run_id = assistant_create_thread_and_run(user_input)
    run_object = assistant_wait_for_run(thread_id, run_id)

    message_object_list = assistant_list_message(thread_id)
    answer = message_object_list[0]["content"][0]["text"]["value"]

    return answer
