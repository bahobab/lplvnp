import os
from config import db, base_url
from models import Image

# Data to initialize database
IMAGE = [
    {
        "description": "glouglou",
        "format": "landscape",
        "subject": "animal",
        "season": "summer",
        "image_url": base_url + "/4804d66c-0322-4edf-a1ec-426ccb674107.jpg",
        "comments": "Nice",
        "stars": "1",
        "name": "4804d66c-0322-4edf-a1ec-426ccb674107.jpg"
    },
    {
        "description": "scurrel",
        "format": "landscape",
        "subject": "human",
        "season": "winter",
        "image_url": base_url + "/1821a76-a2db-499c-b803-f4eab9483e72.jpg",
        "comments": "Nice",
        "stars": "1",
        "name": "31821a76-a2db-499c-b803-f4eab9483e72.jpg"
    }, {
        "description": "blabla",
        "format": "landscape",
        "subject": "nature",
        "season": "fall",
        "image_url": base_url + "/bfc46f06-0458-4a55-aa93-a0c6fe14fe9f.jpg",
        "comments": "Nice",
        "stars": "1",
        "name": "bfc46f06-0458-4a55-aa93-a0c6fe14fe9f.jpg"
    }
]

# Delete database file if it curently exists
if os.path.exists('image.db'):
    os.remove('image.db')

# Create the database
db.create_all()

# Iterate over the IMAGE structure and populate the database

# for image in IMAGE:
#     i = Image(subject=image['subject'], image_name=image['name'], image_format=image['format'], image_url=image['image_url'],
#               season=image['season'], comments=image['comments'], stars=image['stars'], description=image['description'])
#     db.session.add(i)

db.session.commit()
