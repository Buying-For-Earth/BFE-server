from app import db

class ProductOption(db.Model):
    __tablename__ = 'product_option'

    id = db.Column(db.Integer(), primary_key=True)
    product_id = db.Column(db.Integer(), db.ForeignKey('product.id'))
    input_type = db.Column(db.String(255),nullable=False)
    input_option = db.Column(db.JSON,nullable=True)
    order_num = db.Column(db.Integer(), nullable=True) 

    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    