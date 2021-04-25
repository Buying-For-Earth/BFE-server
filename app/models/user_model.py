from app.models.base_model import Base
from app import db
import enum

class Gender(enum.Enum):
    women = 0
    man = 1

class User(Base):
    __tablename__ = 'user'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(64),nullable=False)
    email = db.Column(db.String(64),nullable=False)
    phone = db.Column(db.String(64),nullable=False)
    password = db.Column(db.String(255),nullable=False)
    address = db.Column(db.String(255),nullable=False)
    gender = db.Column(db.Enum(Gender))
    birth = db.Column(db.Date, nullable=True)

    shoppingbasket = db.relationship('ShoppingBasket', backref='shopping_basket', uselist=False)