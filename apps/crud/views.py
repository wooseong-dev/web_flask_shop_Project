from flask import Blueprint, render_template

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
'''
@bp.route('/hello')
def hello_world():
    return 'hello, world!'

@bp.route('/')
def index():
    return 'This is index'
    '''