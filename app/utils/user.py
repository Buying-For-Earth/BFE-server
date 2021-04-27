from flask_restx import Namespace, fields

class UserDto:
    user = Namespace(
        name='User',
        description='유저 관련 API'
    )

    user_signup_field = user.model('signup_field', {
        'name':fields.String(description='유저 이름'),        
        'email':fields.String(description='유저 이메일'),        
        'phone':fields.String(description='유저 전화번호'),        
        'password':fields.String(description='유저 비밀번호'),        
        'address':fields.String(description='유저 주소'),        
        'gender':fields.String(description='유저 성별',  choices=('man','woman')),        
        'birth':fields.String(description='유저 생년월일')        
    })

    user_signin_field = user.model('signin_field', {
        'email':fields.String(description='유저 이메일'),        
        'password':fields.String(description='유저 비밀번호')        
    })