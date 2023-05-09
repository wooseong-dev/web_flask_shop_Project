from flask import Flask, url_for
from markupsafe import escape
from flask import request
from flask import render_template
from flask_pymongo import PyMongo, MongoClient
import pymongo

app = Flask(__name__)
'''
app.config["MONGO_URI"] = "mongodb://localhost:27017/myweb"
mongo = PyMongo(app)'''
'''
conn = pymongo.MongoClient("localhost",27017)
db = conn.test
col = db.members

col.insert_one(test)
'''

client = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = client["test"]
mydb.members.insert_one({"test": 'test'})
print(client.list_database_names())


@app.route("/")
def index():
    online_users = mongo.db.users.find({"online":True})
    return render_template("index.html", online_users=online_users)

@app.route("/write", methods=["GET","POST"])
def board_write():
    if request.method =="POST":
        name = request.form.get("name")
        title = request.form.get("title")
        contents = request.form.get("contents")

        #mongo db data upload
        board = mongo.db.board
        post ={
            "name":name,
            "title":title,
            "contents":contents
        }

        board.insert_one(post)
        return ""
        

        #로그확인

    else:
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



