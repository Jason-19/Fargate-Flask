from . import *
from models.UserModel import User
import jwt
from utils.security import SecurityUserController
sc = SecurityUserController()
auth_route = Blueprint('auth',__name__)




@auth_route.route('/auth/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    user = db.query(User).filter_by(username= username).first()
    print(user.password_hash)
    validate = sc.verify_password(password,user.password_hash)
    
    if not validate or user.username != username:
        return jsonify({"message": "Contraseña incorrecta o usuario no registrado"}), 401
    else:
        token = jwt.encode({'username': username}, 'hola123', algorithm='HS256')
        return jsonify({"message": "Login exitoso","token": token}), 201
   

