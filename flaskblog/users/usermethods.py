import os
import secrets
from PIL import Image
from flask import current_app

def save_picture(form_picture):
    """
    Allows us to change and rezize the default profile picture into a new one
    :return the uploaded picture name resized from the static/Profile_pics folder
    """

    # For different reasons we rename the picture name into a hex of 10 symbols
    random_hex = secrets.token_hex(10)
    # If a picture´s name is Picture.png the text gets split into Picture and .png
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_filename = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/Profile_pics', picture_filename)
    # output_size is in pixels
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_filename
