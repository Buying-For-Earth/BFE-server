from flask_restx import Namespace, fields

class PurchaseDto:
    purchase = Namespace(
        name='Purchase',
        description='구매 API'
    )

    # purchase_field = purchase.model('purchase products', {
    #     'results': fields.List(fields.Nested(product_selected_output_field) , description='장바구니에 담긴 제품 리스트들을 보여줍니다')
    # })

    purchase_field = purchase.model('purchase options', {
        'product': fields.Integer(description='장바구니에 담을 제품 id'),
        'options': fields.List(fields.String, description='제품의 옵션에 대한 정보입니다. 옵션에 대한 추가적인 논의사항이 결정되면 변경할 예정입니다.json'),
    })

    purchase_input_field = purchase.model('purchase products',{
        'products': fields.List(fields.Nested(purchase_field), description='구매할 제품과 제품의 옵션들의 리스트')
    })