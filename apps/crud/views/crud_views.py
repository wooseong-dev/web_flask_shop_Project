from flask import Blueprint

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/hello')
def hello_world():
    return 'hello, world!'

@bp.route('/')
def index():
    return 'This is index'