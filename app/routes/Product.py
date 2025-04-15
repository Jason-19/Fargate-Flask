from . import *
from app.utils.db import get_db
from app.controller.ProductsController import ProductsController

product_route = Blueprint('products',__name__)

Pcontroller = ProductsController

@product_route.route("/products/videogames", methods=['GET'])
def getVideoGamesEndPoint():
    return Pcontroller.getVideoGames(g.db)

@product_route.route("/products/<product_id>/", methods=['GET'])
def getProductsByIdEndpoint(product_id):    
    return Pcontroller.getProductById(g.db,product_id)

@product_route.route("/products/coins", methods=['GET'])
def getCoinsEndPoint():
    
    return Pcontroller.getCoins(g.db)

@product_route.route("/products/coins/games-list", methods=['GET'])
def get_games_with_coins():

    return Pcontroller.getGamesWithCoins(g.db)

@product_route.route("/products/coins/<videogame_name>", methods=['GET'])
def get_coins_for_game(videogame_name:str):
    
    return Pcontroller.getCoinsForGame(g.db,videogame_name)