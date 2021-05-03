from app import db
from app.models.productoption_model import ProductOption

class Product(db.Model):
    __tablename__ = 'product'

    id = db.Column(db.Integer(), primary_key=True)
    category_id = db.Column(db.Integer(), db.ForeignKey('category.id'))
    name = db.Column(db.String(255),nullable=False)
    price = db.Column(db.Integer(),nullable=False)
    detail = db.Column(db.JSON(),nullable=True)
    thumbnail = db.Column(db.Text, nullable=True)

    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    
    productoption = db.relationship('ProductOption', backref='product_option', lazy=True)
    homeprod = db.relationship('HomeProduct', backref='homeproduct', lazy=True)

