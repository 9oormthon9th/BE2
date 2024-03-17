from flask import Blueprint, abort, Flask, request, send_from_directory
import requests
from course_response import course_response

from constant import (
    CHATGPT_SYSTEM_QUERY,
    CHATGPT_USER_QUERY,
    CHATGPT_FOOD_QUERY,
    CHATGPT_ANSWER_QUERY,
)

api_bp = Blueprint("api", __name__, url_prefix="/api")


@api_bp.route("/ready", methods=["GET"])
def ready():
    return {"message": "hello, world!"}


@api_bp.route("/testchatgpt", methods=["GET"])
def call_testchatgpt():
    theme = request.args.get("theme")

    if not theme:
        abort(400)

    return course_response("6")


@api_bp.route("/chatgpt", methods=["GET"])
def call_chatgpt():
    theme = request.args.get("theme")

    if not theme:
        abort(400)

    response = requests.post(
        url="https://api.openai.com/v1/chat/completions",
        headers={"Authorization": "Bearer AA"},
        json={
            "model": "gpt-4",
            "messages": [
                {
                    "role": "system",
                    "content": CHATGPT_SYSTEM_QUERY,
                },
                {"role": "user", "content": CHATGPT_USER_QUERY.format(theme=theme)},
            ],
            "temperature": 0,
        },
        proxies={
            "http": "http://krmp-proxy.9rum.cc:3128",
            "https": "http://krmp-proxy.9rum.cc:3128",
        },
    )

    # response.raise_for_status()
    result = response.json()
    try:
        courseCode = result["choices"][0]["message"]["content"]
        return course_response(courseCode)
    except:
        return "ERROR"

    return "ERROR-NOTRY"


@api_bp.route("/chatgpt2", methods=["GET"])
def call_chatgpt2():
    food = request.args.get("food")

    if not food:
        abort(400)

    response = requests.post(
        url="https://api.openai.com/v1/chat/completions",
        headers={"Authorization": "Bearer AA"},
        json={
            "model": "gpt-4",
            "messages": [
                {
                    "role": "system",
                    "content": CHATGPT_FOOD_QUERY,
                },
                {"role": "user", "content": CHATGPT_ANSWER_QUERY.format(food=food)},
            ],
            "temperature": 0,
        },
        proxies={
            "http": "http://krmp-proxy.9rum.cc:3128",
            "https": "http://krmp-proxy.9rum.cc:3128",
        },
    )

    # response.raise_for_status()
    return response.json()


# Custom CORS middleware
@api_bp.after_request
def add_cors_headers(response):
    # Allow requests from any origin
    response.headers["Access-Control-Allow-Origin"] = "*"
    # Allow credentials (cookies, authorization headers, etc.) to be included in the request
    response.headers["Access-Control-Allow-Credentials"] = "true"
    # Specify allowed headers
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    # Specify allowed methods
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
    return response


if __name__ == "__main__":
    app = Flask(__name__)
    app.register_blueprint(api_bp)
    app.run(host="0.0.0.0", port=5000)
