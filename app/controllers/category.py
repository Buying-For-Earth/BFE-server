from flask_restx import Resource, Namespace, fields
from app.utils.category import *

from app.services.category_service import get_products_by_category_id, get_all_category

api = CategoryDto.category
category_result_field = CategoryDto.category_result_field
category_list_field = CategoryDto.category_list_field

@api.route('/<int:category_id>')
class Category(Resource):
    @api.response(200, 'Success', category_result_field)
    def get(self,category_id):
        """ 카테고리별 제품리스트를 보여주는 api 입니다 """

        prod = get_products_by_category_id(category_id)

        return{
            "results": prod
        },200

@api.route('/all')
class AllCategory(Resource):
    @api.response(200, 'Success', category_list_field)
    def get(self):
        """ 모든 카테고리를 보여주는 api 입니다 """

        cate = get_all_category()

        return{
            "list":cate
        },200