from . import *
from controller.ShoppingCartController import ShoppingCartController
sc = ShoppingCartController
shoppingcart_route = Blueprint('shoppingcart',__name__)

@shoppingcart_route.route("/shoppingcart", methods=['POST'])
def get_shoppingcartEndpoint():
    return sc.get_shoppingcart(g.db)    

@shoppingcart_route.route("/shoppingcart/update", methods=['POST'])
def update_shoppingcartEndpoint():
    return sc.update_shoppingcart(g.db)

# @shoppingcart_route.route("/shoppingcart/add", methods=['POST'])
# def add_shoppingcartEndpoint():
#     return sc.add_shoppingcart(g.db)