from app import db

class HomeCategory(db.Model):
    __tablename__ = 'home_category'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255),nullable=False)
    is_published = db.Column(db.Boolean, default=True)
    
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    products = db.relationship('HomeProduct', backref='home_product', lazy=True)