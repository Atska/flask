from flask import Blueprint, render_template, flash, url_for, redirect, abort
from flaskblog import db
from flaskblog.posts.forms import PostForm
from flaskblog.models import Post
from flask_login import current_user, login_required

posts = Blueprint('posts', __name__)

@posts.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    """
    function for creating new posts
    :return:
    """
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post was successful.', 'success')
        return redirect(url_for('main.home'))
    return render_template('New_post.html', title='New Post', form=form, legend='Update Post')

@posts.route("/post/<int:post_id>")
def post(post_id):
    """
    function for showing a post
    :param post_id: id of the post in our database
    :return: the post on the website
    """
    post=Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)

@posts.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    """

    :return:
    """
    post=Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post was successfully updated.', 'success')
        return redirect(url_for('posts.post', post_id=post_id))
    form.title.data = post.title
    form.content.data = post.content
    return render_template('New_post.html', title='Update Post', form=form,
                           legend='Update Post')

@posts.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    """
    function for deleting post with a Modal in post.html
    :param post_id: id of the post in the db
    :return: redirect to the front page 'home'
    """
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('main.home'))
