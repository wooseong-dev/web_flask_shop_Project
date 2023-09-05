from flask import Blueprint, render_template, redirect, url_for
# db import
from apps.app import db
# User Class import
from apps.crud.models import User
from apps.crud.forms import UserForm


#bp = Blueprint('main', __name__, url_prefix='/')

#blueprint로 crud 앱 생성
crud = Blueprint(
    "crud",
    __name__,
    template_folder="templates",
    static_folder="static",
)

# index 엔드포인트를 작성하고 index.html 반환
@crud.route("/")
def index():
    return render_template("crud/index.html")


@crud.route("/sql")
def sql():
    db.session.query(User).all()
    return "콘솔 로그를 확인해 주세요"

@crud.route("/users/new", methods=["GET", "POST"])
def create_user():
    # UserForm을 인스턴스화한다.
    form = UserForm()
    # 폼의 값을 검증한다.
    if form.validate_on_submit():
        # 사용자를 작성한다.
        user = User(
            username=form.username.data,
            email=form.email.data,
            passsword=form.password.data,
        )
        
        #사용자를 추가하고 커밋한다.
        db.session.add(user)
        db.session.commit()

        #사용자의 일람 화면으로 리다이렉트한다.
        return redirect(url_for("crud.users"))
    return render_template("crud/create.html", form=form)

'''
@bp.route('/hello')
def hello_world():
    return 'hello, world!'

@bp.route('/')
def index():
    return 'This is index'
    '''