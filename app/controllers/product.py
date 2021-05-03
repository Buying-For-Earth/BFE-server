from flask_restx import Resource, Namespace, fields
from app.utils.product import *

from app.services.product_service import get_product_by_id

api = ProductDto.product
product_thumbnail_output_field = ProductDto.product_thumbnail_output_field
product_detail_output_field = ProductDto.product_detail_output_field

@api.route('/<int:prod_id>')
class Product(Resource):
    @api.response(200, 'Success', product_detail_output_field)
    def get(self, prod_id):
        """ 제품 상세 정보를 보여주는 api 입니다 """
        
        prod = get_product_by_id(prod_id)

        return prod,200