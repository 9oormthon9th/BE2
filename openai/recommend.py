from openai.api import course_recommend_pipeline
from openai.recommend_old import recommend_food as recommend_food_old


def recommend_course(user_input: str):
    courseCode = course_recommend_pipeline(user_input)
    return courseCode


def recommend_food(user_input: str):
    foodRecommendation = recommend_food_old(user_input)

    return foodRecommendation
