from flask import Flask, url_for
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def index():
    return "hello"

@app.route("/<name>/")
def hello(name):
    return f"hello, {escape(name)}!"
'''
@app.route("/user/<username>/")
def show_user_profile(username):
    return f'User {escape(username)}'
'''
@app.route("/post/<int:post_id>/")
def show_post(post_id):
    return f'Post {post_id}'

@app.route('/path/<path:subpath>/')
def show_subpath(subpath):
    return f'Subpath {escape(subpath)}'

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

@app.route('/login')
def login():
    return 'login'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))






