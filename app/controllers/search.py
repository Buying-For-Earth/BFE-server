from flask_restx import Resource, Namespace, fields
from app.utils.search import *

api = SearchDto.search
search_result_field = SearchDto.search_result_field

parser = api.parser()
parser.add_argument('search_keyword', type=str, help='검색 키워드', required=True)
parser.add_argument('page', type=int, help='검색 결과 페이지', default=1)
parser.add_argument('order_by', type=str, help='검색 결과 정렬방법', default='name', choices=('name', 'purchase'))

@api.route('')
class Search(Resource):
    @api.expect(parser)
    @api.response(200, 'Success', search_result_field)
    def get(self):
        """ 제품 검색 결과들을 보여주는 api 입니다 """

        return{
            "":""
        },200