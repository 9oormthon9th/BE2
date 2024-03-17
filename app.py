from flask import Blueprint, abort, Flask, request
from course_response import course_response
from openai.recommend import recommend_course, recommend_food

api_bp = Blueprint("api", __name__, url_prefix="/api")


@api_bp.route("/ready", methods=["GET"])
def ready():
    return {"message": "hello, world!"}


@api_bp.route("/test/course", methods=["GET"])
def mock_course():
    theme = request.args.get("theme")

    if not theme:
        abort(400)

    courseCode = "6"
    return course_response(courseCode)


@api_bp.route("/course", methods=["GET"])
def gpt_course():
    theme = request.args.get("theme")

    if not theme:
        abort(400)

    courseCode = recommend_course(user_input=theme)
    return course_response(courseCode)


@api_bp.route("/food", methods=["GET"])
def gpt_food():
    food = request.args.get("food")

    if not food:
        abort(400)

    result = recommend_food(user_input=food)
    return result


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


def create_app():
    app = Flask(__name__)
    app.register_blueprint(api_bp)
    return app


if __name__ == "__main__":
    # For local development
    app = create_app()
    app.run(host="0.0.0.0", port=5000)
