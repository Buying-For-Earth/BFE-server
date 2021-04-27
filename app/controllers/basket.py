from flask_restx import Resource, Namespace, fields
from app.utils.basket import *

api = BasketDto.basket
basket_field = BasketDto.basket_field
basket_input = BasketDto.basket_input

@api.route('')
class Basket(Resource):
    @api.doc(security='apikey')
    @api.response(200, 'Success', basket_field)
    @api.response(401, 'Not Authorized')
    def get(self):
        """ 장바구니 정보를 보여주는 api 입니다 """

        return{
            "":""
        },200

    @api.doc(security='apikey')
    @api.expect(basket_input)
    @api.response(201, 'Success')
    @api.response(401, 'Not Authorized')
    @api.response(404, 'product not found')
    @api.response(400, 'option must selected') #수량 선택
    def post(self):
        """ 장바구니에 제품을 담는 api 입니다 """

        return{
            "":""
        },201