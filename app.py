from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from main import config

db = SQLAlchemy()
migrate = Migrate()

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))
    question = db.relationship('Question', backref=db.backref('answer_set'))
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    #orm
    # $ flask db init
    db.init_app(app)
    migrate.init_app(app, db)

    #blueprint
    from main.views import main_views
    app.register_blueprint(main_views.bp)

    return app