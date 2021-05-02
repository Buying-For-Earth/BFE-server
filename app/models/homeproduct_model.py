from app.models.base_model import Base
from app import db

class HomeProduct(Base):
    __tablename__ = 'home_product'

    id = db.Column(db.Integer(), primary_key=True)
    home_category_id = db.Column(db.Integer(), db.ForeignKey('home_category.id'))
    product_id = db.Column(db.Integer(), db.ForeignKey('product.id'))
