from flask_restx import Resource, Namespace, fields
from app.utils.category import *

api = CategoryDto.category
category_result_field = CategoryDto.category_result_field

parser = api.parser()
parser.add_argument('category', type=str, help='카테고리 선택', choices=('칫솔', '세제', '추가예정'), required=True)

@api.route('')
class Category(Resource):
    @api.expect(parser)
    @api.response(200, 'Success', category_result_field)
    def get(self):
        """ 카테고리별 제품리스트를 보여주는 api 입니다 """

        return{
            "":""
        },200