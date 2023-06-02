from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello world"

@app.route("/hello/<name>", 
           methods=["GET", "POST"],
           endpoint="hello-endpoint")
def hello(name):
    return f"Hello {name}!"

@app.route("/name/<name>")
def show_name(name):
    #변수를 템플릿 엔진에게 건넨다.
    return render_template("index.html", name=name)

# flask 2 이후부터는 @app.get("/hello"), @app.post("hello") 기술 가능
# @app.get("/")
# @app.post("/")
# @app.route("/", methods=["GET", "POST"])