from app.models.base_model import Base
from app import db

class Product(Base):
    __tablename__ = 'product'

    id = db.Column(db.Integer(), primary_key=True)
    category_id = db.Column(db.Integer(), db.ForeignKey('category.id'))
    name = db.Column(db.String(255),nullable=False)
    price = db.Column(db.Integer(),nullable=False)
    detail = db.Column(db.JSON(),nullable=True)

    shoppingbasket = db.relationship('ShoppingBasket', backref='shopping_basket', lazy=True)
    productoption = db.relationship('ProductOption', backref='product_option', lazy=True)