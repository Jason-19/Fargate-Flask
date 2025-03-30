
from . import *
from models.UserModel import Order, User, OrderItem, PaymentMethod,Wallet,ShoppingCart,Saving
from models.ProductModel import Product
order_route = Blueprint('order',__name__)

    
@order_route.route('/order',methods=['GET'])
def get_orders():
    orders = db.query(Order).all()
    return jsonify([order.serialize() for order in orders])

@order_route.route('/order/<id_order>',methods=['GET'])
def getOrderById(id_order):
    orders= db.query(Order).where(Order.id_order == id_order)
    response = [orders.serialize() for orders in orders]
    
    if not (len(response)):
        return jsonify({"message":"Order no encntrada","order":response}),200
    return jsonify(response), 200


@order_route.route('/order/item/<user_id>', methods=['GET'])
def get_user_orders(user_id):
    
    orders = db.query(Order).filter_by(id_user=user_id).all()
    order_list = []
    for order in orders:
        order_items = db.query(OrderItem).filter_by(id_order=order.id_order).all()
        items = []
        
        for item in order_items:
            product = db.query(Product).get(item.id_product)
            
            items.append({
                'id_product': item.id_product,
                'name': product.name,
                'quantity': item.quantity,
                'price': item.price
            })
        
        order_list.append({
            'id_order': order.id_order,
            'total': order.total,
            'status': order.status,
            'created_at': order.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'items': items
        })
    return order_list

#  post 
@order_route.route('/orders/<current_user>', methods=['POST'])
def create_order(current_user):
    request_data = request.get_json()
    
    print(current_user)
    print(request_data)
    payment_method = db.query(PaymentMethod).filter_by(id_payment=request_data['id_payment'], id_user=current_user).first()
    
    if not payment_method:
        return jsonify({'message': 'Metodo de pago no encontrado'}), 404
    
    new_order = Order(
        id_user=current_user.id_user,
        id_payment= request_data['id_payment'],
        total=0, 
        status='pending'
    )
    # db.session.add(new_order)
    db.session.commit()
    
    total = 0
    order_items = []
    
    for item in request_data['items']:
        product =db.query(Product).get(item['id_product'])
        if not product:
            return jsonify({'message': 'Producto no encontrado',}), 401
    
        order_item = OrderItem(
            id_order=new_order.id_order,
            # id_product=product
            quantity=item['quantity'],
            price=product.price
        )
        db.session.add(order_item)
        order_items.append({
            'name': product.name,
            'quantity': item['quantity'],
            'price': float(product.price)
        })
        
        total += product.price * item['quantity']
    
    new_order.total = total
    # db.session.commit()
    
    savings_amount = total * 0.05
    
    wallet = db.query(Wallet).filter_by(id_user=current_user).first()
    wallet.balance += savings_amount
    print(wallet.balance)
    # db.session.commit()
    
    new_saving = Saving(
        id_user=current_user,
        id_order=new_order.id_order,
        amount_saved=savings_amount
    )
    # db.session.add(new_saving)
    # db.session.commit()
    
    cart = db.query(ShoppingCart).filter_by(id_user=current_user).first()
    cart.products = []
    # db.session.commit()
    
    return jsonify({
        'message': 'Order created successfully!',
        'order_id': new_order.id_order,
        'total': float(total),
        'savings': float(savings_amount),
        'items': order_items
    }), 201