from os import path, remove, listdir
from pathlib import Path

from flask import (
    make_response,
    send_file,
    abort,
    jsonify
)

from sqlalchemy import or_, and_

from config import db

from models import (
    Image,
    ImageSchema
)

basedir = path.abspath(path.dirname(__file__))
file_dir = 'images/dest/'

# Delete database file if it curently exists
# if path.exists('image.db'):
#     remove('image.db')

# db.create_all()
# db.session.commit()

# @login_required


def get_all():
    """
    call get_image() with random querystring values
    ::return 10::
    """

    images = Image.query.order_by(Image.name).all()

    image_schema = ImageSchema(many=True)

    return image_schema.dump(images)


def get_all_n(n):
    """
    n: integer

    return:: array of dictionaryies
    """

    if n > 10:
        n = 10

    images = Image.query.filter(Image.name).limit(n).all()
    return ImageSchema().dump(images, many='many')


def get_one(image_name):
    """
    scan querystring
    return 5 images by default
    """
    image = Image.query.filter(Image.name == image_name).one_or_none()

    if image is not None:
        image_schema = ImageSchema()
        return image_schema.dump(image)

    else:
        abort(404, 'Image does not exist for image name: {image_name}'.format(
            image_name=image_name))


def get_subject_n(subject, n):
    """
    subject: string
    n: integer

    return:: array of dictionaryies
    """

    # print('>>>', subject, n)

    if n > 10:
        n = 10

    images = Image.query.filter(Image.subject == subject).limit(n).all()
    return ImageSchema().dump(images, many='many')


def add(image):
    print(image['name'])

    image_exists = find_image(image['name'])
    # print('>>>>', image)
    if image_exists is False:
        abort(401, "Image already exists. Try another image")

    schema = ImageSchema()
    new_image = schema.load(image, session=db.session)

    db.session.add(new_image)
    db.session.commit()

    return schema.dump(new_image), 201


def get_image(image_name):
    """
    Look in the images folder to find the file.
    if exists:
        return image, 200
    else:
        return file not found, 400
    """

    image = find_image(image_name)
    if image is False:
        return 'File not found', 400
    return send_file(image), 200


def find_image(file_name):
    """
    checks if file exists

    :return the file is found:
    :else return False

    """

    image = file_dir + file_name
    # if path.isfile(image):
    if Path(image).is_file():
        print(image)
        return image
    else:
        return False


def search(subject, portrait, landscape, winter, spring, summer, autumn):
    """
    http://www.leeladharan.com/sqlalchemy-query-with-or-and-like-common-filters
    https://www.sqlitetutorial.net/
    """

    orientation = []
    season = []

    if portrait == 'true':
        orientation.append('portrait')
    if landscape == 'true':
        orientation.append('landscape')

    if winter == 'true':
        season.append('winter')
    if spring == 'true':
        season.append('spring')
    if summer == 'true':
        season.append('summer')
    if autumn == 'true':
        season.append('autumn')

    # try:
    images = Image.query.filter(and_(Image.subject == subject, or_(Image.season.in_(
        season)), Image.orientation.in_(
        orientation))).all()

    return ImageSchema().dump(images, many='many')

    # except:
    # abort(404, "Search failed")


# ****************** TEST ************************************
"""
curl -X POST -H "Content-Type: application/json" -d '{
    "stars": 2,"image_format":"portrait","image_name":"wewe-dddd-ujujujj.jpg","subject":"test",
    "comments": "great pix", "season":"fall"
}' http://localhost:5001/api/v1/images

"""

# IMAGES = {
#     "4804d66c-0322-4edf-a1ec-426ccb674107": {
#         "name": "scurrel",
#         "format": "landscape",
#         "subject": "animal",
#         "season": "witer",
#         "comments": "Nice",
#         "stars": "1",
#         "image_name": "4804d66c-0322-4edf-a1ec-426ccb674107"
#     },
#     "31821a76-a2db-499c-b803-f4eab9483e72": {
#         "name": "scurrel",
#         "format": "landscape",
#         "subject": "animal",
#         "season": "witer",
#         "comments": "Nice",
#         "stars": "1",
#         "image_name": "31821a76-a2db-499c-b803-f4eab9483e72"
#     }, "bfc46f06-0458-4a55-aa93-a0c6fe14fe9f": {
#         "name": "scurrel",
#         "format": "landscape",
#         "subject": "animal",
#         "season": "witer",
#         "comments": "Nice",
#         "stars": "1",
#         "image_name": "bfc46f06-0458-4a55-aa93-a0c6fe14fe9f.jpg"
#     }
# }


# def getAll():
#     return [[IMAGES[key] for key in IMAGES.keys()]]
