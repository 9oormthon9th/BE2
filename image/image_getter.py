import base64


def get_photo(courseNum):
    with open("image/photo/" + courseNum + ".png", "rb") as f:
        encoded_image = base64.b64encode(f.read())
    return encoded_image


def get_struc(courseNum):
    with open("image/struc/" + courseNum + ".png", "rb") as f:
        encoded_image = base64.b64encode(f.read())
    return encoded_image
