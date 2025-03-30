
from . import *
from models.UserModel import User, Order

user_route = Blueprint('user',__name__) 

class UsersController():
    def get_user(db:Session):
        return db.query(User).all()

    def create_user(db:Session, user):
        db_user =User(**user.model_dump())
        logs.info("adde",db_user)
        print(db_user)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user


@user_route.route("/user/all",methods=['GET'])
def getuser():
    user= db.query(User).all()
    user_list = [user.serialize() for user in user]
    return jsonify(user_list), 200

@user_route.route("/user/<id_user>/",methods=['GET'])
def getuserById(id_user):
    user= db.query(User).where(User.id_user == id_user).first()
    return jsonify(user.serialize()), 200


@user_route.route("/user/order/<id_user>",methods=['POST'])
def getuserOrderById(id_user):
    orderUser= db.query(Order).where(User.id_user == id_user).all()
    user_list = [user.serialize() for user in orderUser]
    return jsonify(user_list), 200

@user_route.route("/user",methods=['POST'])
def createuser():
    data = request.json
    user = UsersController.create_user(db,data)
    return jsonify(user.serialize()), 200