from flask_restx import Namespace, fields
from app.utils.product import ProductDto

class SearchDto:
    search = Namespace(
        name='Search',
        description='제품 검색 API'
    )

    search_result_field = search.model('search results', {
        'results': fields.List(fields.Nested(ProductDto.product_thumbnail_output_field) , description='검색 결과를 보여줍니다')
    })
