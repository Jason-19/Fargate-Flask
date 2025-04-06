from . import *

class User(Base):
    __tablename__ = "users"
    user_id = Column(String(50), primary_key=True, default=lambda: str(uuid.uuid4()))
    first_name = Column(String(50), nullable=True)
    last_name = Column(String(50), nullable=True)
    username = Column(String(50), unique=True, nullable=True)
    email = Column(String(50), unique=True, nullable=True)
    password_hash = Column(String(50), nullable=True)
    phone = Column(String(20), nullable=True)
    birth_date = Column(Date, nullable=True)
    created_at = Column(TIMESTAMP, server_default='CURRENT_TIMESTAMP')
    avatar = Column(String(255), nullable=True)
    
    def serialize(self):
        return {
        'user_id': self.user_id,
        'first_name': self.first_name,
        'last_name': self.last_name,
        'username': self.username,
        'email': self.email,
        'phone': self.phone,
        'birth_date': self.birth_date,
        'created_at': self.created_at,
        'avatar': self.avatar
    }

class PaymentMethod(Base):
    __tablename__ = "payment_methods"
    
    id_payment = Column(Integer, primary_key=True)
    id_user = Column(Integer, nullable=False)
    card_number = Column(String(16), nullable=False)
    card_holder = Column(String(255), nullable=False)
    expiration_date = Column(Date, nullable=False)
    cvv = Column(String(4), nullable=False)
    created_at = Column(TIMESTAMP, default="CURRENT_TIMESTAMP")
    
    def serialize(self):
        return {
            "id_payment ": self.id_payment,
            "id_user ": self.id_user,
            "card_number ": self.card_number,
            "card_holder ": self.card_holder,
            "expiration_date ": self.expiration_date,
            "cvv ": self.cvv,
            "created_at ": self.created_at,
        }


class Order(Base):
    __tablename__ = 'orders'
    
    id_order = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    id_user = Column(String(36), ForeignKey('users.id_user'))
    id_payment = Column(String(36), ForeignKey('payment_methods.id_payment'))
    total = Column(Numeric(10, 2), nullable=False)
    savings = Column(Numeric(10, 2), nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp())
    status = Column(Enum('pending', 'completed', 'cancelled'), default='pending')
    description = Column(JSON)
    
    user = relationship('User', backref='orders')
    payment_method = relationship('PaymentMethod', backref='orders')
    
    def serialize(self):
        return {
            'id_order': self.id_order,
            'id_user': self.id_user,
            'id_payment': self.id_payment,
            'total': float(self.total),            
            'savings': float(self.savings),
            'created_at': str(self.created_at),
            'status': self.status,
            'description': self.description,
        }


class OrderItem(Base):
    __tablename__ = "order_items"
    
    id_order_item = Column(Integer, primary_key=True)
    id_order = Column(Integer)
    id_product = Column(Integer)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    def serialize(self):
        return {
            "id_order_item": self.id_order_item,
            "id_order": self.id_order,
            "id_product": self.id_product,
            "quantity": self.quantity,
            "price": self.price,
        }

class Wallet(Base):
    __tablename__ = "wallet"
    
    id_wallet = Column(Integer, primary_key=True)
    id_user = Column(Integer)
    balance = Column(Float, default=0.00)
    created_at = Column(TIMESTAMP, default="CURRENT_TIMESTAMP")

    def serialize(self):
        return {
            "id_wallet": self.id_wallet,
            "id_user": self.id_user,
            "balance": self.balance,
            "created_at": self.created_at,
        }
        
class Saving(Base):
    __tablename__ = "savings"
    
    id_saving = Column(Integer, primary_key=True)
    id_user = Column(Integer , nullable=False)
    id_order = Column(Integer, nullable=False)
    amount_saved = Column(Float, nullable=False)
    created_at = Column(TIMESTAMP, default="CURRENT_TIMESTAMP")


    def serialize(self):
        return {
            "id_saving": self.id_saving,
            "id_user": self.id_user,
            "id_order": self.id_order,
            "amount_saved": self.amount_saved,
            "created_at": self.created_at,
        }


class SavingPlan(Base):
    __tablename__ = "saving_plans"
    
    id_plan = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    min_amount = Column(Float, nullable=False)
    min_transactions = Column(Integer, nullable=False)
    annual_interest = Column(Float, nullable=False)

    def serialize(self):
        return {
            "id_plan": self.id_plan,
            "name": self.name,
            "min_amount": self.min_amount,
            "min_transactions": self.min_transactions,
            "annual_interest": self.annual_interest
        }


class UserSavingPlan(Base):
    __tablename__ = "user_saving_plans"
    
    id_user = Column(Integer, primary_key=True)
    id_plan = Column(Integer, primary_key=True)
    start_date = Column(TIMESTAMP, default="CURRENT_TIMESTAMP")
    

    def serialize(self):
        return {
            "id_user": self.id_user,
            "id_plan": self.id_plan,
            "start_date": self.start_date,
            
        }

class ShoppingCart(Base):
    __tablename__ = "shopping_cart"
    
    id_cart = Column(Integer, primary_key=True)
    id_user = Column(Integer)
    products = Column(JSON, nullable=False)
    created_at = Column(TIMESTAMP, default="CURRENT_TIMESTAMP")
    updated_at = Column(TIMESTAMP, default="CURRENT_TIMESTAMP")

    def serialize(self):
        return {
            "id_cart": self.id_cart,
            "id_user": self.id_user,
            "products": self.products,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }


class InterestHistory(Base):
    __tablename__ = "interest_history"
    
    id_interest = Column(Integer, primary_key=True)
    id_user = Column(Integer, nullable=False)
    id_wallet = Column(Integer, nullable=False)
    interest_amount = Column(Float, nullable=False)
    calculated_at = Column(TIMESTAMP, default="CURRENT_TIMESTAMP")


    def serialize(self):
        return {
            "id_interest": self.id_interest,
            "id_user": self.id_user,
            "id_wallet": self.id_wallet,
            "interest_amount": self.interest_amount,
            "calculated_at": self.calculated_at,
        }

    
