from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from . import config

db = SQLAlchemy()
migrate = Migrate()

def create_app(): #애플리케이션 팩토리
    app = Flask(__name__)
    app.config.from_object(config)

    #ORM
    db.init_app(app)
    migrate.init_app(app,db)

    #blueprint
    from .views import main_views
    app.register_blueprint(main_views.bp)
    
    if __name__ == '__main__':
        app.run('127.0.0.1', 5000, debug=True)
    #return app