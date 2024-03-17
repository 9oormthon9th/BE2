# This is helper script to create knowledge base for the chatbot
import pandas as pd
from data_getter import get_description

available_courses = [
    "1",
    "1-1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "7-1",
    "8",
    "9",
    "10",
    "10-1",
    "11",
    "12",
    "13",
    "14",
    "14-1",
    "15",
    "16",
    "17",
    "18",
    "18-1",
    "18-2",
    "19",
    "20",
    "21",
]


def list_courses():
    """Returns list of courses"""
    descriptionDf = pd.read_csv("data/description.csv", sep="\\", index_col="course")
    print(descriptionDf.index.tolist())


def create_knowledge():
    """Creates knowledge base for the chatbot"""
    with open("data/knowledge.md", "w") as file:
        for course in available_courses:
            file.write(f"# {course}\n\n")
            file.write(f"{get_description(course)}\n\n")


if __name__ == "__main__":
    create_knowledge()
