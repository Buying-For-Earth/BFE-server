from flask_restx import Resource, Namespace, fields
from app.utils.user import *

api = UserDto.user
user_signup_field = UserDto.user_signup_field
user_signin_field = UserDto.user_signin_field

@api.route('/signup')
class SignUp(Resource):
    @api.expect(user_signup_field)
    @api.response(201, 'Success')
    @api.response(400, 'enter informations')
    def post(self):
        """ 회원가입 API 입니다 """

        return{
            "":""
        },201

@api.route('/signin')
class SignIn(Resource):
    @api.expect(user_signin_field)
    @api.response(201, 'Success')
    @api.response(404, 'user not found')
    @api.response(400, 'fill all values')
    def post(self):
        """  로그인 api 입니다 """

        return{
            "":""
        },201