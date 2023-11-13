# demo_data/populate_demo_data.py
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from models import Product, Sale, Inventory
from datetime import datetime

# MySQL database connection
DATABASE_URL = "mysql://your_username:your_password@localhost/your_database"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db = SessionLocal()

# Sample data
products_data = [
    {"name": "Product1", "price": 19.99, "category": "Electronics"},
    {"name": "Product2", "price": 29.99, "category": "Clothing"},
   
]

sales_data = [
    {"product_id": 1, "quantity": 10, "amount": 199.90, "sale_date": datetime.now()},
    {"product_id": 2, "quantity": 5, "amount": 149.95, "sale_date": datetime.now()},
   
]

inventory_data = [
    {"product_id": 1, "quantity": 100, "last_updated": datetime.now()},
    {"product_id": 2, "quantity": 50, "last_updated": datetime.now()},
    
]


for product_info in products_data:
    product = Product(**product_info)
    db.add(product)

for sale_info in sales_data:
    sale = Sale(**sale_info)
    db.add(sale)

for inventory_info in inventory_data:
    inventory = Inventory(**inventory_info)
    db.add(inventory)

# Commit the changes
db.commit()
