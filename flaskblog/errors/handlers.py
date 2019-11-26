from flask import Blueprint, render_template

# Custom Error Pages https://flask.palletsprojects.com/en/1.0.x/patterns/errorpages/

errors = Blueprint('errors', __name__)

@errors.app_errorhandler(404)
def Not_Found_404():
    """
    error when the requested URL was not found on the server
    :return:
    """
    return render_template('errors/404.html'), 404
