from . import *


class Product(Base):
    __tablename__ = "products"
    
    id_product = Column(String(36), primary_key=True)
    name = Column(String(255), nullable=False)
    description = Column(JSON)
    price = Column(Numeric(10, 2), nullable=False)
    image_url = Column(String(255))
    created_at = Column(TIMESTAMP, default=func.current_timestamp())
    
    id_category = Column(String(36), ForeignKey('categories.category_id'))
    category = relationship('Category', backref='products')
    
    def serialize(self):
        return{
            "id_product": self.id_product,
            "name": self.name,  
            "description": self.description,
            "price": self.price,
            "image_url":self.image_url,
            "created_at": self.created_at,
            'id_category': self.id_category,
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