from datetime import datetime

from apps.app import db
from werkzeug.security import generate_password_hash

# db.Model 상속 User 클래스 생성
class User(db.Model):
    # 테이블명 지정
    __tablename__ = "users"
    # 컬럼을 정의한다
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, index=True)
    email=db.Column(db.String, unique=True, index=True)
    password_hash = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    
    # 비밀번호 설정을 위한 속성값
    @property
    def password(self):
        raise AttributeError("읽어들일 수 없음")
    #비밀번호 설정을 위한 Setter 함수로 해시화한 비밀번호 설정
    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)


