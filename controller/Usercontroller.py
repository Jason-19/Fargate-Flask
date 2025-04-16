from . import *
from flask import jsonify
from models.UserModel import User
from sqlalchemy.orm import Session

class UsersController:
    # @staticmethod
    def get_user(db:Session):
        try:
            user= db.query(User).all()   
            if not user:
                return jsonify({"message": "There are no users is empty"}), 404
            return jsonify([u.serialize() for u in user]), 200
        except Exception as e:
            print(e)    
            return jsonify({"message": "Error in query"}), 404
        
       
    
    
    def getUserById(db:Session,user_id):
        user= db.query(User).where(User.user_id == user_id).first()
        
        if not user:
            return jsonify({"message": "User not found"}), 404
        return jsonify(user.serialize()), 200