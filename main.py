"""
Web app for a blog
"""
from flaskblog import create_app

start_app=create_app()

if __name__ == '__main__':
    start_app.run(debug=True)
