from flask_restx import Namespace, fields

class HelloDto:
    Print_hello = Namespace(
        name='Hello',
        description='예시로 만든 Hello API'
    )

    hello_field = Print_hello.model('Hello',{
        'message': fields.String(description='print hello message')
    })