from . import * 
from models.UserModel import Wallet

wallet_route = Blueprint('wallet',__name__)

@wallet_route.route('/wallet', methods=['GET'])
def get_wallet():
    try:
       wallet = db.query(Wallet).all()
    except Exception as e:
        return jsonify({'message': str(e)}), 500
    
    if not wallet:
        return jsonify({'message': 'No existen Wallet'}), 404
    return jsonify([w.serialize() for w in wallet])

@wallet_route.route('/wallet/<id_user>', methods=['GET'])
def get_wallet_by_id_user(id_user):
    
    print(f"Buscando wallet.... {id_user}")
    try:
        wallet = db.query(Wallet).where(Wallet.id_user == id_user).first()
    except Exception as e:
        print(f"Error al buscar wall {str(e)}")
        return jsonify({'message': str(e)}), 500
    
    if not wallet:
        print("Wallet no encontrada")
        return jsonify({'message': 'Wallet no encontrada', 'wallet':[]}), 404
    
    print("Wallet encontrada")
    return jsonify({
        'id_wallet': wallet.id_wallet,
        'balance': float(wallet.balance),
        'created_at': wallet.created_at
    })
