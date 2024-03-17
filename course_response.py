from image.image_getter import get_photo, get_struc
from data.data_getter import get_info, get_description


def course_response(courseCode: str):
    """Returns a JSON string containing course information
    :param courseCode: example: "6", "18-1"
    :type courseCode: str
    """
    result = get_info(courseCode)
    result["description"] = get_description(courseCode)
    result["image"] = get_photo(courseCode)
    result["image2"] = get_struc(courseCode)

    return result.to_json(force_ascii=False)
