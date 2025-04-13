from flask import Flask, jsonify, render_template, send_from_directory
from flask_cors import CORS
from routes import Orders,Product,User,Auth,wallet, Payment
from flask_swagger_ui import get_swaggerui_blueprint
app = Flask(__name__)
CORS(app)

swaggerui_blueprint = get_swaggerui_blueprint(
    '/docs',
    '/openapi.json',
    config={ 
        'app_name': "Gamer Vault LTS"
    }
)
app.register_blueprint(Auth.auth_route)
app.register_blueprint(User.user_route)
app.register_blueprint(Product.product_route)     
app.register_blueprint(Orders.order_route)
app.register_blueprint(wallet.wallet_route)
app.register_blueprint(Payment.payment_route)
app.register_blueprint(swaggerui_blueprint, url_prefix='/docs')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/health')
def health_check():
    return jsonify({"status": "healthy"}), 200

@app.route('/openapi.json')
def openapi(): 
    return send_from_directory('.', 'openapi.json', mimetype='application/json')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
