from flask_restx import Namespace, fields
from app.utils.product import ProductDto

class HomeDto:
    home = Namespace(
        name='Home',
        description='홈 화면을 보여주는 API'
    )

    home_recommand = home.model('recommand_products_list',{
        'name': fields.String(description='홈 화면에 보일 제품 추천 이름입니다. ex) MD 추천'),
        'products': fields.List(fields.Nested(ProductDto.product_thumbnail_output_field), description='md 추천 상품 항목을 보여줍니다'),
        'order_num': fields.Integer(description="정렬 순서입니다.")
    })

    home_output_field = home.model('home_page',{
        'list': fields.List(fields.Nested(home_recommand), description='홈 화면에 보여지는 상품들의 목록입니다')
    })

    