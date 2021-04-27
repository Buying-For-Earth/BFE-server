from flask_restx import Namespace, fields

class ProductDto:
    product = Namespace(
        name='Product',
        description='제품 정보와 관련된 API'
    )

    product_thumbnail_output_field = product.model('Product Thumbnail',{
        'image': fields.String(description='변경될 예정입니다. 사진을 어떻게 전송할지 리서치가 필요합니다'),
        'name': fields.String(description='제품의 이름입니다'),
        'price': fields.Integer(description='제품의 가격입니다'),
    })