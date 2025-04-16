import jwt
from models.UserModel import User
from flask import request,g, jsonify
from datetime import date, datetime
from utils.security import SecurityUserController
sc = SecurityUserController()


class AuthController:
    
    def login(data):
        data = request.json
        username = data.get('username')
        password = data.get('password')
        user = g.db.query(User).filter_by(username= username).first()
        
        if not user:
            return jsonify({"message": "Unregistered User"}), 401
        validate = sc.verify_password(password,user.password_hash)
        
        if not validate or user.username != username:
            return jsonify({"message": "Registered password or unregistered user"}), 401
        else:
            token = jwt.encode({'user_id': user.user_id}, 'ggeasy', algorithm='HS256')
            return jsonify({"token": token}), 200



    def register(data):
        data = request.json
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        # confirm_password', 'terms_accepted'
        required = ['username', 'birth_date', 'email', 'password_hash']
        
        for field in required:
            if field not in data or not data[field]:
                return jsonify({'error': f'{field} required'}), 400
            
        # if data['password'] != data['confirm_password']:
        #     return jsonify({'error': 'Passwords do not match'}), 400
        
        # if not data['terms_accepted']:
        #     return jsonify({'error': 'You must accept the terms and conditions'}), 400
        
        # mayor 18 mvp
        today = date.today()
        age = today.year - datetime.strptime(data['birth_date'], '%Y-%m-%d').year
        
        if age < 18:
            return jsonify({'error': 'You must be at least 18 years old'}), 400 
        
        #  validar el hasheo de la contraseña (nvp)
        password_hash = sc.hash_password(data['password_hash'])
        data['password_hash'] = password_hash
        
        try:
            #usuario o email ya existe en la bd
            if g.db.query(User).filter_by(username=data['username']).first():
                return jsonify({'error': 'The username is already in use'}), 400
            
            if g.db.query(User).filter_by(email=data['email']).first():
                return jsonify({'error': 'The email is already registered'}), 400
            
            user = User(**data)
            g.db.add(user)
            g.db.commit()
            g.db.refresh(user)
            
        except Exception as e:
            g.db.rollback()
            return jsonify({'error': str(e)}), 500
        
        return jsonify({'message': 'Registered successfully'}), 201