from flask_restx import Resource, Namespace, fields
from app.utils.home import *

from app.services.home_service import get_homepage

api = HomeDto.home
home_output_field = HomeDto.home_output_field

@api.route('')
class Home(Resource):
    @api.response(200, 'Success', home_output_field)
    def get(self):
        """ 홈 화면을 구성하는 상품들의 목록을 보여주는 api 입니다 """

        home = get_homepage()

        return{
            "list": home
        },200