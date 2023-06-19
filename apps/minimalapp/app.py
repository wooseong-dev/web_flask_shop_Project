from flask import Flask, render_template, url_for, current_app, g, request, redirect, flash
from email_validator import validate_email, EmailNotValidError
import logging
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
# SECRET_KEY 추가
app.config["SECRET_KEY"] = "tOOR4vFdlHoGEo3sbUNj"
#로그레벨 설정
app.logger.setLevel(logging.DEBUG)
#리다이렉트 중단하지 않도록 설정
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
#DebugToolbarExtension에 애플리케이션을 설정한다.
toolbar = DebugToolbarExtension(app)



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

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/contact/complete", methods=["GET", "POST"])
def contact_complete():
    if request.method =='POST':

        # form 속성을 사용해서 폼의 값을 취득한다.
        username = request.form["username"]
        email = request.form["email"]
        description = request.form["description"]

        #입력 체크

        is_valid = True

        if not username:
            flash("사용자명은 필수입니다.")
            is_valid = False
        
        if not email:
            flash("이메일 입력은 필수입니다.")
            is_valid = False
        
        try:
            validate_email(email)
        except EmailNotValidError:
            flash("메일 주소의 형식으로 입력해 주세요")
            is_valid = False
        
        if not description:
            flash("문의 내용은 필수입니다.")
            is_valid = False
        
        if not is_valid:
            return redirect(url_for("contact"))

        
        #이메일을 보낸다(나중 구현)

        #문의 완료 엔드포인트로 리다이렉트
        flash("문의해 주셔서 감사합니다.")
        return redirect(url_for("contact_complete"))
    return render_template("contact_complete.html")

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