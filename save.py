from flask import Flask, url_for, current_app, g
from markupsafe import escape
from flask import request
from flask import render_template
from flask_pymongo import PyMongo, MongoClient
import pymongo
from main import config
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/myweb"
mongo = PyMongo(app)



'''
client = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = client["test"]
mydb.members.insert_one({"test": 'test'})
print(client.list_database_names())
'''

def get_db():
    db = getattr(g, "_database", None)

    if db is None:

        db = g._database = PyMongo(current_app).db

    return db

@app.route("/")
def index():
    online_users = mongo.db.users.find({"online":True})
    return render_template("index.html", online_users=online_users)

@app.route("/write", methods=["GET","POST"])
def board_write():
    if true:
        return render_template("write.html")
    
@app.route("/user/<username>")
def user_profile(username):
    user = mongo.db.users.find_one_or_404({"_id":username})
    return render_template("user.html", user=user)

    


'''
@app.route("/<name>/")
def hello(name):
    return f"hello, {escape(name)}!"

@app.route("/user/<username>/")
def show_user_profile(username):
    return f'User {escape(username)}'

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

'''
if __name__ == '__main__':
    app.run('127.0.0.1', 5000, debug=True)



