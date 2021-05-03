from app import db

class HomeProduct(db.Model):
    __tablename__ = 'home_product'

    id = db.Column(db.Integer(), primary_key=True)
    home_category_id = db.Column(db.Integer(), db.ForeignKey('home_category.id'))
    product_id = db.Column(db.Integer(), db.ForeignKey('product.id'))

    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
