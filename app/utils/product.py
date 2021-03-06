from flask_restx import Namespace, fields

class ProductDto:
    product = Namespace(
        name='Product',
        description='제품 정보와 관련된 API'
    )

    product_thumbnail_output_field = product.model('Product Thumbnail',{
        'id': fields.Integer(description='제품의 아이디입니다'),
        'thumbnail': fields.String(description='img인 경우 이미지가 저장된 s3의 주소'),        
        'name': fields.String(description='제품의 이름입니다'),
        'price': fields.Integer(description='제품의 가격입니다'),
    })

    product_detail_content = product.model('Product_detail_text',{
        'type': fields.String(description='본문 타입, text, img가 있습니다'),
        'text': fields.String(description='본문'),        
        'url': fields.String(description='img인 경우 이미지가 저장된 s3의 주소'),        
    })

    product_option_content = product.model('Product_option',{
        'order_num':fields.Integer(description='해당 옵션의 정렬 순서입니다'),
        'input_option':fields.String(description='해당 옵션에 대한 json 정보입니다')
    })

    product_detail_output_field = product.model('Product Detail',{
        'thumbnail': fields.String(description='썸네일의 url입니다'),
        'name': fields.String(description='제품의 이름입니다'),
        'category': fields.String(description='제품의 카테고리입니다'),
        'price': fields.Integer(description='제품의 가격입니다'),
        'detail': fields.List(fields.Nested(product_detail_content), description='본문 구성입니다'),
        'options': fields.List(fields.Nested(product_option_content), description='제품의 옵션 입니다')
    })

    
