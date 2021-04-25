from app.models.base_model import Base
from app import db

class Category(Base):
    __tablename__ = 'category'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(64),nullable=False)

    products = db.relationship('Product', backref='product', lazy=True)