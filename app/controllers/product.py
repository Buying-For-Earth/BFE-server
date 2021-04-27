from flask_restx import Resource, Namespace, fields
from app.utils.product import *

api = ProductDto.product
product_thumbnail_output_field = ProductDto.product_thumbnail_output_field
product_detail_output_field = ProductDto.product_detail_output_field

@api.route('')
class Product(Resource):
    @api.response(200, 'Success', product_detail_output_field)
    def get(self):
        """ 제품 상세 정보를 보여주는 api 입니다 """

        return{
            "":""
        },200