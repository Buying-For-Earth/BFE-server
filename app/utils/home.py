from flask_restx import Namespace, fields
from app.utils.product import ProductDto

class HomeDto:
    home = Namespace(
        name='Home',
        description='홈 화면을 보여주는 API'
    )

    home_output_field = home.model('home',{
        'MD 추천': fields.List(fields.Nested(ProductDto.product_thumbnail_output_field) , description='md 추천 상품 항목을 보여줍니다'),
        '새롭게 입점된 제품': fields.List(fields.Nested(ProductDto.product_thumbnail_output_field), description='새롭게 입점된 제품 상품 항목을 보여줍니다'),
        '2020女 많이 찾는 제품': fields.List(fields.Nested(ProductDto.product_thumbnail_output_field), description='2020女 많이 찾는 제품 상품 항목을 보여줍니다')
    })