from app import db
from app.models.product_model import Product
from app.models.productoption_model import ProductOption
from app.models.category_model import Category

def get_product_by_id(prod_id):
    prod = db.session.query(Category, Product, ProductOption).\
        filter(Product.id == ProductOption.product_id).\
        filter(Product.category_id == Category.id).\
        filter(Product.id == prod_id).\
        all()

    return jsonfy_get_product_by_id(prod)
    
def jsonfy_get_product_by_id(prod):
    options = []
    category, product, po = prod[0]
    for c, p, po in prod:
        options.append({
            'order_num': po.order_num,
            'input_option': po.input_option
        })

    return {
        'thumbnail': product.thumbnail,
        'name': product.name,
        'category': category.name,
        'price': product.price,
        'detail': product.detail,
        'options': options
    }
