# from flask_restx import Namespace, fields

# class SelectedProductDto:
#     product = Namespace(
#         name='SelectedProduct',
#         description='옵션이 선택된 제품 정보와 관련된 API'
#     )

#     product_selected_output_field = product.model('Product Selected',{
#         'image': fields.String(description='변경될 예정입니다. 사진을 어떻게 전송할지 리서치가 필요합니다'),
#         'name': fields.String(description='제품의 이름입니다'),
#         'options': fields.List(fields.String, description='제품의 옵션에 대한 정보입니다. 옵션에 대한 추가적인 논의사항이 결정되면 변경할 예정입니다.json'),
#         'price': fields.Integer(description='제품의 가격입니다'),
#     })

#     # product_detail_output_field = product.model('Product Detail',{
#     #     'image': fields.String(description='변경될 예정입니다. 사진을 어떻게 전송할지 리서치가 필요합니다, 썸네일입니다'),
#     #     'name': fields.String(description='제품의 이름입니다'),
#     #     'category': fields.String(description='제품의 카테고리입니다'),
#     #     'price': fields.Integer(description='제품의 가격입니다'),
#     #     'detail': fields.String(description='변경될 예정입니다. 사진을 어떻게 전송할지 리서치가 필요합니다, 제품 상세정보입니다'),
#     # })