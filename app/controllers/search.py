from flask import request
from flask_restx import Resource, Namespace, fields
from app.utils.search import *

from app.services.search_service import get_products_by_keyword

api = SearchDto.search
search_result_field = SearchDto.search_result_field

parser = api.parser()
parser.add_argument('search_keyword', type=str, help='검색 키워드', required=True)

@api.route('')
class Search(Resource):
    @api.expect(parser)
    @api.response(200, 'Success', search_result_field)
    def get(self):
        """ 제품 검색 결과들을 보여주는 api 입니다 """
        keyword = request.args.get('search_keyword')
        prods = get_products_by_keyword(keyword)

        return{
            "results":prods
        },200