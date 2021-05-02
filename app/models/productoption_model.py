from app.models.base_model import Base
from app import db

class ProductOption(Base):
    __tablename__ = 'product_option'

    id = db.Column(db.Integer(), primary_key=True)
    product_id = db.Column(db.Integer(), db.ForeignKey('product.id'))
    input_type = db.Column(db.String(255),nullable=False)
    input_option = db.Column(db.JSON,nullable=True)
    order_num = db.Column(db.Integer(), nullable=True) # 자동증가 가능한지

    