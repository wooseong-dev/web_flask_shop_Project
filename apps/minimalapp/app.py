from flask import Flask, render_template, url_for, current_app, g, request

app = Flask(__name__)

#여기에서 호출하면 오류가 된다.
#print(current_app)

#애플리케이션 컨텍스트를 취득하여 스택에 push한다
ctx = app.app_context()
ctx.push()

# current_app에 접근할 수 있게 된다.
print(current_app.name)
# >> apps.minimalapp.app

#전역 임시 영역에 값을 설정한다.
g.connection = "connection"
print(g.connection)
# >> connection


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

with app.test_request_context("/users?updated=true"):
    #true가 출력된다.
    print(request.args.get("updated"))
    #/
    print(url_for("index"))
    # /hello/world
    print(url_for("hello-endpoint", name="world"))
    #/name/AK?page=1
    print(url_for("show_name", name="AK", page="1"))
    #/static/style.css
    print(url_for("static", filename="style.css"))

# flask 2 이후부터는 @app.get("/hello"), @app.post("hello") 기술 가능
# @app.get("/")
# @app.post("/")
# @app.route("/", methods=["GET", "POST"])