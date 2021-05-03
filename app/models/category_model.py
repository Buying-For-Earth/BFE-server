from app import db

class Category(db.Model):
    __tablename__ = 'category'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(64),nullable=False)

    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    products = db.relationship('Product', backref='product', lazy=True)