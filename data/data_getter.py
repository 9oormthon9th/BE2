import pandas as pd

olleDf = pd.read_csv("data/olle.csv")
descriptionDf = pd.read_csv("data/description.csv", sep="\\")


def get_info(courseCode: str):
    """Returns data from olle.csv
    :rtype: DataFrame
    """
    result = olleDf[olleDf["올레길 코스 번호"] == (courseCode + "코스")]
    result = result.iloc[0]
    return result


def get_description(courseCode: str):
    """Returns description from description.csv
    :rtype: str
    """
    description = descriptionDf[descriptionDf["course"] == (courseCode)]
    description = description.iloc[0]["description"]
    return description
