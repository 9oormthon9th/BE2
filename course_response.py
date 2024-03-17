import pandas as pd
from image.image_getter import get_photo, get_struc
from data.data_getter import get_info, get_description


def course_response(courseNum: str):
    result = get_info(courseNum)  # type: pd.Series
    result["description"] = get_description(courseNum)
    result["image"] = get_photo(courseNum)
    result["image2"] = get_struc(courseNum)

    return result.to_json()
