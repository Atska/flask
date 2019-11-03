class Configuration:
    """
    SECRET_Key via library secrets with token_hex(16)
    Database_URI (sqlite, postgresql, oracle, mysql) = https://docs.sqlalchemy.org/en/13/core/engines.html
    """
    SECRET_KEY = 'fe415753a29c110c4ed102c3a2603c7c'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# os.environ.get('SECRET_KEY')
# os.environ.get('SQLALCHEMY_DATABASE_URI')
# set up an environment in windows for these values
