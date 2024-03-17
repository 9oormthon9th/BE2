import base64
from flask import Blueprint, abort, Flask, request, send_from_directory
import pandas as pd
import requests

from constant import (
    CHATGPT_SYSTEM_QUERY,
    CHATGPT_USER_QUERY,
    CHATGPT_FOOD_QUERY,
    CHATGPT_ANSWER_QUERY,
)

data = pd.read_csv("data/olle.csv")
data1 = pd.read_csv("data/description.csv", sep="\\")
print(data)
print(data1)

api_bp = Blueprint("api", __name__, url_prefix="/api")


@api_bp.route("/images/<path:courseNumber>")
def serve_image(courseNumber):
    return send_from_directory("images", courseNumber + ".jpg")


@api_bp.route("/ready", methods=["GET"])
def ready():
    return {"message": "hello, world!"}


def course_info(courseNum):
    result = data[data["올레길 코스 번호"] == (courseNum + "코스")]
    result = result.iloc[0]

    description = data1[data1["course"] == (courseNum)]
    description = description.iloc[0]["description"]
    result["description"] = description

    with open("images/" + courseNum + ".png", "rb") as f:
        encoded_image = base64.b64encode(f.read())
        result["image"] = encoded_image
    with open("image2/" + courseNum + "Struc.png", "rb") as f1:
        encoded_image2 = base64.b64encode(f1.read())
        result["image2"] = encoded_image2

    return result.to_json()


@api_bp.route("/testchatgpt", methods=["GET"])
def call_testchatgpt():
    theme = request.args.get("theme")

    if not theme:
        abort(400)

    return course_info("6")


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
        courseNum = result["choices"][0]["message"]["content"]
        return course_info(courseNum)
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
