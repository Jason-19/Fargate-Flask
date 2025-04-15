from flask import jsonify
from app.models.ProductModel import Product,Category
from sqlalchemy.orm import Session
import json


class ProductsController:
    
    def getVideoGames(db:Session):
        
        category_videogames = db.query(Category).filter(Category.name.ilike("%videogame%")).first()
        if not category_videogames:
            return jsonify({'message': 'Category Videogames not found in database'}), 404
        
        product = db.query(Product).filter(Product.category_id == category_videogames.category_id).all()
        if not product: 
            return jsonify({'message': 'Product not found'}), 404
        
        return jsonify([p.serialize() for p in product]),200
        
    
    def getProductById(db:Session, product_id):
        
        product = db.query(Product).filter(Product.product_id == product_id).first()
        if not product:
            return jsonify({'message': 'Product not found'}), 404
        
        return jsonify(product.serialize()),200
    
    def getCoins(db:Session):
        games = [] 
        category = db.query(Category).filter(Category.name.ilike("%coins%")).first()
        if not category:    
            return jsonify({'message': 'Category coins not found in database'}), 404
        coins = db.query(Product).join(Category).filter(Category.name == "coins").all()
        
        if not coins:
            return jsonify({'message': 'Coins not found in database'}), 404
        
        for product in coins:
                
            description = product.prod_description
        
            if isinstance(description, str):
                try:
                    description = json.loads(description)
                except json.JSONDecodeError:
                    description = {}

            game_name = description.get('game')
            if game_name:
                games.append({
                    "game_name": game_name,
                    "product_id": product.product_id,
                    "image_url": product.image_url,
                    "category_name": category.name
                })
        return jsonify(games), 200

    def getGamesWithCoins(db:Session):
        coin_category = db.query(Category).filter(Category.name.ilike("%coins%")).first()
    
        if not coin_category:
            return jsonify({"error": "Coin category not found"}), 404

        products = db.query(Product).filter(Product.category_id == coin_category.category_id).all()

        games_list = []
        for product in products:
            description = product.prod_description
            if isinstance(description, str):
                try:
                    description = json.loads(description)
                except json.JSONDecodeError:
                    continue
            
            if 'game' in description:
                game_data = {
                    "game": description['game'],
                    "image_url": product.image_url
                }
                games_list.append(game_data)

        unique_games = []
        seen = set()
        for game in games_list:
            key = (game["game"], game["image_url"])
            if key not in seen:
                seen.add(key)
                unique_games.append(game)

        unique_games_sorted = sorted(unique_games, key=lambda x: x["game"])

        return jsonify(unique_games_sorted), 200
    
    def getCoinsForGame(db:Session, videogame_name:str):
        coin_category = db.query(Category).filter(Category.name == "coins").first() 
        if not coin_category:
            return jsonify({"error": "Coin category not found"}), 404
        
        products = db.query(Product).filter(Product.category_id == coin_category.category_id).all()

        filtered_products = [product for product in products if product.prod_description.get('game') == videogame_name]
        
        if not filtered_products:
            return jsonify({"error": f"No coins found for game {videogame_name}"}), 404

        return jsonify([product.serialize() for product in filtered_products]), 200
    