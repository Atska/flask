"""
This is a ReadMe for the Flask Web App or blog
"""

# commands to start flask in terminal
set FLASK_APP = main.py
flask run

# Debugmode for live updates
set FLASK_Debug=1

# Als Alternative dazu:
if __name__ == "__main__":
    app.run(debug=True)

-------------------------------
# Adding new headers in flaskblog.py
@app.route("/'Insert Header")
def about():
    return "<h1>Insert Header/>"

# Templates for html codes. Make a new folder "templates" and create html files.
import render_template('Insert name html file')
import render_template('Insert name html file', title='Insert title')
# in dir. templates we create the layout to bundle repeated code from home and about into one html

# for bootstrap "https://getbootstrap.com/docs/4.3/getting-started/introduction/" to prettify blog
# Required meta tags + Bootstrap CSS belong to layout.html.
# Javascript in layout.html

# add snippets for the web app
# Put these navigation and main html files inside layout.html in the body section
# create static folder and insert main.css
# Refer main.css in layout.html:
<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='main.css')}}">

# We need access to "forms" so people can create account on the website and log in  and log out.
# -> pip install flask-wtf and create forms.py
# create registration form with a class that inherits from FlaskForm
# create validators for username (e.g. 2-20 characters so people dont use 50) in a list
# create the Login_form class
# create a secret key in the flaskblog.py with terminal: import secrets; secrets.token_hex(16); 16 = number of bytes
# in flaskblog import both classes from forms and create the route

# create register.html and login.html
# To allow registration in flask go to flaskblog.py and to the app.route of register and add methods to it
# Validate the submit with if clause and import flash which flashes a message
# add html (line 45 in layout.html) which flashes the message in register function (Success)
# When there is an error when the user register then he needs a message for it -> register.html start line 11
# copy the finished register.html to login.html and remove the username block (line 11) and confirm_password
# add remember into the code in login.html (line 37) and messages
# The next focus is in flaskblog.py the function login: Validation
# In layout use url_for for better maintenance of code

# flask-sqlalchemy is deployed for using different databases without changing the code so much
# import SQLAlchemy amd add the app Configuration Key and create a db file with the specific command
# create SQLALCHEMY(app) and the database classes.
# SQL databases are created with classes; 'sqlite:///site.db' for
# Aim is a unique id for the user: Create primary keys and these are integer
# the username/email must only have 15 letters and conditions are that its unique and cant be null (must have username)
# image_file is for profile pictures; Multiple user can have same picture and we create a default picture
# add password column
# __repr__ shows how we want it to look like
# create new table with class Post (id, title, content, dated_posted)
# there will be no author in class Post because an author can have many post but a post can only have one author
# posts (in class User) means there is a relationship with class Post
# lazy=True argument will allow sqlalchemy to lead the data in one go

# move the classes User and Post to models.py and import those classes in flaskblog.py
# move bigger applications in a package for maintainability and avoid collision with module names
# create __init__ and put in all imports and configs in it
# create routes to put routes in there
# regulate all imports so everything works

# Aim is to hash password so noone can access them if they are in a database ->pip install flask-bcrypt
# add it to __Init__
# in routes import db and bcrypt and add hashed_password into def register
# create an instance of the user and use the hashed_password as the password because we want to hash it
# db.create.all(), db.session.add(user), db.session.commit() to add user into the data base and commit it
# there is an error when you try to register with the same username and email
# create validations in Registerforms in forms.py by creating two functions
# query the database in search for the username and whether its a duplicate. (.first()) returns the first result.

# Now the focus is on a login system with flask-login (pip install) to manage user sessions
# add this LoginManager(app) to __init__ and import it in models; add the function load_user
# load UserMixin, a class for representing users. We need these methods. Let User class inherit it.
# go to routes function login and filter database if there is the email available wit user.query[...]
# if user and correct password ->login_user
# add current_user.is_authenticated so logged in user can join

# import log_out in flask_login and create a logout-route and add a logout bar in our navigation
# in layout.html (line 35) add the if clause whether user is authenticated and name it logout
# add @login_required decorator in functions logout and account as a condition
# in __init__ add login_manager.login_view and login_manager.login_message_category so user who
  are nor logged in cant access account site/or get an info that they have to log in

# create a layout in account.html with snippets and add current username and email
# in routes/function account and url_for the default picture and add it to render_template
# in account.html add image_file

# add features update user_name/email and upload custom pictures -> create forms for it (UpdateAccountForm)
# we have to check whether the current_user already exist
# in routes update function account with if and elif clause so we can update email and username with ease

# next is update profile-picture with imports FileField and FileAllowed from fileask_wtf.file
# in class UpdateAccountForm add picture and add the html code (line44)
# create a new function which saves the profile picture in the user´s account
# import secrets and os and create function save_picture in routes.
# secrets will give the picture name a random hex, os will give us the filename and the name of the extension
# in function account picture_file and current_user.image_file
# we need to scale picture so they dont overload or server - pip install Pillow and import the Image class from routes
# in function save_picture three img to resize picture and add it to the account function in the if clause

# to allow visitors to view, update or delete post we have to create a New_post.html
# just copy it from login and remove email for title and password for content
# remove unnecessary html and in layout-navigation add New Posts
# to save new posts in our database in function new_post db.session etc.
# in function home() add Post.query.all() to query all posts

# create in routes the function update_post to update our posts
# add form.title.data and form.content.data to visualize the content of our post
# next we need to create in post.html the buttons for updating and delting post
# on the bootstrap site copy the modal bootstrap and change it for our use
# create delete_post function in routes

# for pagination we need to alter the home.html with a for loop to visualize the pages
# in routes create user_posts and create the html user_posts based on post.html


Important! Packages! with __init__
