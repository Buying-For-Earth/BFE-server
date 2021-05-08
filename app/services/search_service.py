from app import db
from app.models.product_model import Product
import re

def get_products_by_keyword(keyword):
    prods = db.session.query(Product).\
        filter(Product.name.op('regexp')(f'.*{keyword}.*')).\
        all()

    print(prods)
    return jsonfy_get_products_by_keyword(prods)
    
def jsonfy_get_products_by_keyword(prods):
    li = []
    for p in prods:
        li.append({
            "id": p.id,
            "thumbnail": p.thumbnail,
            "name": p.name,
            "price": p.price
        })

    return li