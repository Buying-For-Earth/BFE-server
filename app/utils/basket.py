from flask_restx import Namespace, fields



class BasketDto:
    basket = Namespace(
        name='Basket',
        description='장바구니 API'
    )
    product_selected_output_field = basket.model('selected products(수정예정)',{
        'image': fields.String(description='변경될 예정입니다. 사진을 어떻게 전송할지 리서치가 필요합니다'),
        'name': fields.String(description='제품의 이름입니다'),
        'options': fields.List(fields.String, description='제품의 옵션에 대한 정보입니다. 옵션에 대한 추가적인 논의사항이 결정되면 변경할 예정입니다.json'),
        'price': fields.Integer(description='제품의 가격입니다'),
    })

    basket_field = basket.model('basket products', {
        'results': fields.List(fields.Nested(product_selected_output_field) , description='장바구니에 담긴 제품 리스트들을 보여줍니다')
    })

    basket_input = basket.model('input basket', {
        'product': fields.Integer(description='장바구니에 담을 제품 id'),
        'options': fields.List(fields.String, description='제품의 옵션에 대한 정보입니다. 옵션에 대한 추가적인 논의사항이 결정되면 변경할 예정입니다.json'),
    })
