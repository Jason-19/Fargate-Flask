from . import *
from models.UserModel import PaymentMethod
payment_route = Blueprint('payment',__name__)

@payment_route.route("/payment", methods=['GET'])
def create_payment_method():
    payment_method = db.query(PaymentMethod).all()
    return jsonify([p.serialize() for p in payment_method]), 200