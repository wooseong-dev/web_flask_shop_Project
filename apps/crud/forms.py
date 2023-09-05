from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, StringField, ValidationError
from wtforms.validators import DataRequired, Email, Length

# 사용자 신규 작성과 사용자 편집 폼 클래스
class UserForm(FlaskForm):
    # 사용자 폼의 username 속성의 라벨과 검증을 설정한다.
    username = StringField(
        "사용자명",
        validators=[
            DataRequired(message="사용자명은 필수입니다. "),
            Length(max=30, message="30문자 이내로 입력해 주세요. "),
        ],
    )
    
    # 사용자폼 email 속성의 라벨과 검증을 설정한다.
    email = StringField(
        "메일 주소",
        validators=[
            DataRequired(message="메일 주소는 필수입니다."),
            Email(message="메일 주소의 형식으로 입력해 주세요. "),
        ],
    )

    #사용자 폼 password 속성의 라벨과 검증을 설정한다.

    password = PasswordField("비밀번호",validators=[DataRequired(message="비밀번호는 필수입니다. ")])
    '''
    # validate_+filed명
    def validate_password(self,password):
        if not password.data:
            #오류시 raise 해당 Error 발생
            raise TypeError("이거 왜 틀린거")'''

    #사용자폼 submit의 문구를 설정한다.
    submit = SubmitField("신규 등록")

