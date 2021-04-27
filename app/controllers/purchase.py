from flask_restx import Resource, Namespace, fields
from app.utils.purchase import *

api = PurchaseDto.purchase
purchase_input_field = PurchaseDto.purchase_input_field

@api.route('')
class Purchase(Resource):
    @api.doc(security='apikey')
    @api.expect(purchase_input_field)
    @api.response(201, 'Success')
    @api.response(401, 'Not Authorized')
    @api.response(404, 'product not found')
    @api.response(400, 'option must selected') #수량 선택
    def post(self):
        """  제품을 구매하는 api 입니다 """

        return{
            "":""
        },201