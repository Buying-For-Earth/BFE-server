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

    category_field = category.model('category', {
        'id': fields.Integer(description='카테고리의 db pk입니다'),
        'name': fields.String(description='카테고리의 이름입니다')
    })

    category_list_field = category.model('all_category', {
        'list': fields.List(fields.Nested(category_field), description='생성된 카테고리들의 리스트입니다')
    })