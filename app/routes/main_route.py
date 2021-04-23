from flask import Blueprint, request
from flask_restx import Api

from app.controllers.hello import *

bp = Blueprint('main', __name__)
api = Api(bp)

api.add_resource(Hello, '/hello')
# @bp.route('/hello')
# def hello():
#     return 'hello!'