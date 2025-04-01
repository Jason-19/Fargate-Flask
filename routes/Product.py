from . import *
from models.ProductModel import Product,Category


product_route = Blueprint('product',__name__)

class ProductsController():
    
    def get_products(db:Session, limit:int, last_product = None):
        
        if last_product is None:
            return jsonify({ "Error":"parameter last_id is requered"}),404
        product = db.query(Product).filter(Product.id_product > last_product).limit(limit).all()
        return jsonify([product.serialize() for product in product]),200
        
    
    def getProductById(db:Session,id_product):
        product = db.query(Product).filter(Product.id_product == id_product).first()
        return jsonify(product.serialize()),200
    
    def create_product(db:Session, product):
        db_product =Product(**product)
        db.add(db_product)
        db.commit()
        # db.refresh(db_product)
        return db_product


@product_route.route("/product", methods=['GET'])
def getProducts():
    last = request.args.get('last')
    limit = request.args.get('limit', default=10)
    category = request.args.get('category',default=None)
    print(last, limit,category)
    
    # products = ProductsController.get_products(db,limit)
    # last_product_id = [product['id_product'] for product in products][-1]
    
    # print(last_product_id)
    # return last_product_id
    return ProductsController.get_products(db,limit,category)

# @product_route.route("/product/games", methods=['GET'])
# def getProducts():
#     last = request.args.get('last')
#     limit = request.args.get('limit', default=10)
#     print(last, limit)
    
#     # products = ProductsController.get_products(db,limit)
#     # last_product_id = [product['id_product'] for product in products][-1]
    
#     # print(last_product_id)
#     # return last_product_id
#     return ProductsController.get_products_coins(db,limit)

@product_route.route("/product", methods=['POST'])
def createProducts():
    ProductsController.create_product(db, request.json)
    return jsonify({"message": 'Product Created'}),201


@product_route.route("/product/<id_product>", methods=['GET'])
def getProductsById(id_product):
    return jsonify(ProductsController.getProductById(db,id_product)),200


