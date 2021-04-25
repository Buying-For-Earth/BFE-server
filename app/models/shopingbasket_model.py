from app.models.base_model import Base
from app import db

class ShoppingBasket(Base):
    __tablename__ = 'shpping_basket'

    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    product_id = db.Column(db.Integer(), db.ForeignKey('product.id'))
    option = db.Column(db.JSON(), nullable=True)

    