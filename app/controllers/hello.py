from flask_restx import Resource

class Hello(Resource):
    def get(self):
        return {
            "message": "hello!"
        },200
