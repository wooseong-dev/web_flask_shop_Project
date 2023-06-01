'''
import pymongo

test = {
    "이름" : "양우성",
    "나이" : 30,
    "거주지":"서울특별시",
    "키":170,
    "프로필사진":[
        "a.jpg",
        "b.jpg"
    ]

}

conn = pymongo.MongoClient("localhost",27017)
db = conn.test
col = db.members

col.insert_one(test)'''
'''
import sys
import os

dir = os.path.realpath(__file__) #경로 불러오기
print(dir)

print(sys.path)
'''
#sys.path.append("C:\Users\wooseong\Documents\개인파일\IT_SourceCode\main_project")

#sys.path.append("C:\Users\wooseong\Documents\개인파일\IT_SourceCode\main_project")
#sys.path.append('\\wudong.synology.me@ssl@5006\DavWWWRoot\두번째 저장소\개인파일\IT_SourceCode\')
'''
import os
BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'mydb.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False'''

import app

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