from app.models.base_model import Base
from app import db

class HomeCategory(Base):
    __tablename__ = 'home_category'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255),nullable=False)
    is_published = db.Column(db.Boolean, default=True)

    products = db.relationship('HomeProduct', backref='home_product', lazy=True)