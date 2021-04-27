from flask_restx import Namespace, fields
from app.utils.product import ProductDto

class CategoryDto:
    category = Namespace(
        name='Category',
        description='카테고리별 제품리스트를 받아오는 API'
    )

    category_result_field = category.model('category results', {
        'results': fields.List(fields.Nested(ProductDto.product_thumbnail_output_field) , description='카테고리별 제품들을 보여줍니다')
    })