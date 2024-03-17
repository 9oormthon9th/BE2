import base64


def get_photo(courseCode):
    with open("image/photo/" + courseCode + ".png", "rb") as f:
        encoded_image = base64.b64encode(f.read())
    return encoded_image


def get_struc(courseCode):
    with open("image/struc/" + courseCode + ".png", "rb") as f:
        encoded_image = base64.b64encode(f.read())
    return encoded_image
