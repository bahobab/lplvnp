from flask import (
    send_file,
    abort
)


def get_image(image_name):
    return send_file(image_name), 200
