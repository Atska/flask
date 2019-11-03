from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flaskblog.configuration import Configuration

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = "info"

# If we are importing a module, __name__ is the name of the module
def create_app():
    """
    create the object once and configure the application later to support it
    :return:
    """
    app = Flask(__name__)
    app.config.from_object(Configuration)

    # in flasksqlalchemy-doc
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    # It has to be here otherwise there is a error message!
    from flaskblog.users.routes import users
    from flaskblog.posts.routes import posts
    from flaskblog.main.routes import main
    from flaskblog.errors.handlers import errors

    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app
