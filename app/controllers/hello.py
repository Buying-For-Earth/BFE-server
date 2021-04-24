from flask_restx import Resource, Namespace, fields
from app.utils.hello import *

api = HelloDto.Print_hello
hello_field = HelloDto.hello_field

@api.route('')
class Hello(Resource):
    # @api.doc(responses={200: 'Success'})
    @api.response(200, 'Success', hello_field)
    def get(self):
        """ {"message": "hello"}를 반환하는 간단한 역할입니다. """
        return {
            "message": "hello!"
        }