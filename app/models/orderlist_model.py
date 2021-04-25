from app.models.base_model import Base
from app import db

class OrderList(Base):
    __tablename__ = 'order_list'

    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    product_id = db.Column(db.Integer(), db.ForeignKey('product.id'))
    name = db.Column(db.String(64),nullable=False)
    email = db.Column(db.String(64),nullable=False)
    phone = db.Column(db.String(64),nullable=False)
    address = db.Column(db.String(255),nullable=False)
    memo = db.Column(db.Text(),nullable=True)
    option = db.Column(db.JSON(), nullable=True)
    is_delivery = db.Column(db.Boolean(), default=False)
    