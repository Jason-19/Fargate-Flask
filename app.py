from flask import Flask
from flask_cors import CORS
from routes import Orders,Product,User,Auth,wallet, Payment

app = Flask(__name__)
CORS(app)
app.register_blueprint(Auth.auth_route)
app.register_blueprint(User.user_route)
app.register_blueprint(Product.product_route)     
app.register_blueprint(Orders.order_route)
app.register_blueprint(wallet.wallet_route)
app.register_blueprint(Payment.payment_route)

@app.route('/')
def home():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000,debug=True)
