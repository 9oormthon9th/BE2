from openai.api import chat_completion
from openai.queries import (
    CHATGPT_SYSTEM_QUERY,
    CHATGPT_USER_QUERY,
    CHATGPT_FOOD_QUERY,
    CHATGPT_ANSWER_QUERY,
)


def recommend_course(user_input: str):
    courseCode = chat_completion(
        [
            {
                "role": "system",
                "content": CHATGPT_SYSTEM_QUERY,
            },
            {
                "role": "user",
                "content": CHATGPT_USER_QUERY.format(user_input=user_input),
            },
        ]
    )
    return courseCode


def recommend_food(user_input: str):
    foodRecommendation = chat_completion(
        [
            {
                "role": "system",
                "content": CHATGPT_FOOD_QUERY,
            },
            {
                "role": "user",
                "content": CHATGPT_ANSWER_QUERY.format(user_input=user_input),
            },
        ]
    )
    print(foodRecommendation)

    return foodRecommendation
