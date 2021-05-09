from app import db
from app.models.homecategory_model import HomeCategory
from app.models.homeproduct_model import HomeProduct
from app.models.product_model import Product

def get_homepage():
    home = db.session.query(HomeCategory, HomeProduct, Product).\
        filter(HomeCategory.id == HomeProduct.home_category_id).\
        filter(Product.id == HomeProduct.product_id).\
        filter(HomeCategory.is_published == True).\
        order_by(HomeCategory.order_num).\
        all()
    
    # print(home)
    return jsonfy_get_homepage(home)

def jsonfy_get_homepage(home):
    li = []
    tmp = {}
    for hc, hp, p in home:
        if hc.name not in tmp:
            tmp[hc.name] = {}
            tmp[hc.name]["list"] = []
            tmp[hc.name]["order_num"] = hc.order_num

        tmp[hc.name]["list"].append({
            "id": p.id,
            "thumbnail": p.thumbnail,
            "name": p.name,
            "price": p.price
        })

    # print(tmp)

    for el in tmp:
        li.append({
            "name": el,
            "products": tmp[el]["list"],
            "order_num": tmp[el]["order_num"]
        })
    # print(li)
    return li