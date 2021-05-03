from app import db
from app.models.category_model import Category
from app.models.product_model import Product

def get_products_by_category_id(category_id):

    prod = db.session.query(Category, Product).\
        filter(Category.id == Product.category_id).\
        filter(Category.id == category_id).\
        all()

    return jsonfy_get_products_by_category_id(prod)

def jsonfy_get_products_by_category_id(prod):
    li = []

    for c, p in prod:
        li.append({
            "thumbnail": p.thumbnail,
            "name": p.name,
            "price": p.price
        })
    return li

def get_all_category():

    cate = db.session.query(Category).\
        all()

    return jsonfy_get_all_category(cate)

    
def jsonfy_get_all_category(cate):
    li = []
    for el in cate:
        li.append({
            "id":el.id,
            "name": el.name
        })
    return li
