from flask import Blueprint, request

bp = Blueprint('main', __name__)

@bp.route('/hello')
def hello():
    return 'hello!'