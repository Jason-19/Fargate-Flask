
from . import *
from models.UserModel import User, Order

user_route = Blueprint('users',__name__) 

class UsersController:
    # @staticmethod
    def get_user(db:Session):
        user= db.query(User).all()
        if not user:
            return jsonify({"message": "There are no users is empty"}), 404
        return jsonify([user.serialize() for user in user]), 200
    
    
    def getUserById(db:Session,user_id):
        user= db.query(User).where(User.user_id == user_id).first()
        
        if not user:
            return jsonify({"message": "User not found"}), 404
        return jsonify(user.serialize()), 200
    
    
    def getUserOrderById(db: Session, user_id):
        orderUser= db.query(Order).where(User.user_id == user_id).all()
        user_list = [user.serialize() for user in orderUser]
        return jsonify(user_list), 200
        

ucontroller = UsersController

@user_route.route("/users/all",methods=['GET'])
def getUsersEndpoint():
    return ucontroller.get_user(db)

@user_route.route("/users/<user_id>/",methods=['GET'])
def getUserByIdEndpoint(user_id):
    return ucontroller.getUserById(db,user_id)


@user_route.route("/users/order/<user_id>",methods=['POST'])
def getuserOrderById(user_id):
    return ucontroller.getUserOrderById(db,user_id)
