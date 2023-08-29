from flask import Blueprint, render_template
# db import
from apps.app import db
# User Class import
from apps.crud.models import User



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
    db.session.query(User).get(1)
    return "콘솔 로그를 확인해 주세요"

'''
@bp.route('/hello')
def hello_world():
    return 'hello, world!'

@bp.route('/')
def index():
    return 'This is index'
    '''