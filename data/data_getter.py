import pandas as pd
from typing import Union

olleDf = pd.read_csv("data/olle.csv", index_col="올레길 코스 번호")
descriptionDf = pd.read_csv("data/description.csv", sep="\\", index_col="course")


def get_info(
    courseCode: str,
):
    """Returns data from olle.csv"""
    index = courseCode + "코스"
    result: pd.Series[Union[pd.StringDtype, pd.Float64Dtype, pd.BooleanDtype]] = olleDf.loc[index]  # type: ignore
    # Use Series.info() to see the type of each column

    result = result.copy()  # to avoid SettingWithCopyWarning
    result["올레길 코스 번호"] = index  # index was dropped because of loc. Manually add
    return result


def get_description(courseCode: str):
    """Returns description from description.csv
    :rtype: str
    """
    result: pd.Series[pd.StringDtype] = descriptionDf.loc[courseCode]  # type: ignore
    return result.values[0]
