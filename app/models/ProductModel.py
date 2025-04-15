from . import *


class Product(Base):
    __tablename__ = "products"
    
    product_id = Column(String(50), primary_key=True)
    prod_name = Column(String(50), nullable=False)
    prod_description = Column(JSON)
    prod_price = Column(Numeric(10, 2), nullable=False)
    image_url = Column(String(255))
    created_at = Column(TIMESTAMP, default=func.current_timestamp())
    
    category_id = Column(String(50), ForeignKey('categories.category_id'))
    category = relationship('Category', backref='products')
    
    def serialize(self):
        return{
            "product_id": self.product_id,
            "name": self.prod_name,  
            "description": self.prod_description,
            "price": self.prod_price,
            "image_url":self.image_url,
            "created_at": self.created_at,
            'id_category': self.category_id,
            'category_name': self.category.name
        }

class Category(Base):
    __tablename__ = 'categories'
    
    category_id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String(255), nullable=False, unique=True)
    description = Column(JSON)
    
    def serialize(self):
        return {
            'category_id': self.category_id,
            'name': self.name,
            'description': self.description
        }