from . import *
from flask import jsonify, request
from sqlalchemy.orm import Session
from models.ShoppingCartModel import ShoppingCart

class ShoppingCartController:
    
    def get_shoppingcart(db:Session):
        user_id = request.get_json()
        print(user_id)
        if not user_id['user_id']:
            return jsonify({'error': 'No data provided'}), 400
        try:
            cart = db.query(ShoppingCart).filter_by(user_id = user_id['user_id']).first()
            if not cart:
                return jsonify({'error': 'User does not have a shopping cart'}), 500
            return jsonify(cart.serialize()), 200
        except Exception as e:
            db.rollback()
            return jsonify({'error': str(e)}), 500 
    
    def add_shoppingcart(db:Session):
        user_id = request.get_json()
        if not user_id['user_id']:
            return jsonify({'error': 'No data provided'}), 400
        try:
            user = user_id['user_id']
            newCart = ShoppingCart(**user_id)
            db.add(newCart)
            db.commit()
            db.close()
            return jsonify({"message":"Nuevo carrito registrado"}), 201
        except Exception as e:
            db.rollback()
            return jsonify({'error': str(e)}), 500

    def update_shoppingcart(db:Session):
        cart = request.get_json()
        if not cart:
            return jsonify({'error': 'No data provided'}), 400
        if not cart['user_id']:
            return jsonify({'error': 'User is required'}), 500
        user_id = cart['user_id']
        products = cart['products']
        try:
            user = db.query(ShoppingCart).filter_by(user_id = user_id).first()
            if not user:
                return jsonify({'error': 'User does not have a shopping cart'}), 500
            else:
                db.query(ShoppingCart).filter(user_id == user_id).update({ShoppingCart.products: products})
                db.commit()
                return jsonify({"Mmessage": "Cart Updated", "cart":products}), 200
        except Exception as e:
            db.rollback()
            return jsonify({'error': str(e)}), 500
        
