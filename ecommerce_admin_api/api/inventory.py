# api/inventory.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models.inventory import Inventory
from datetime import datetime
from typing import List

router = APIRouter(prefix="/inventory", tags=["inventory"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_inventory_status(low_stock_threshold: int = 10, db: Session = Depends(get_db)):
    # Get current inventory status and filter low stock items
    inventory_status = db.query(Inventory).all()
    low_stock_items = [item for item in inventory_status if item.quantity < low_stock_threshold]
    return {"inventory_status": inventory_status, "low_stock_items": low_stock_items}

@router.post("/update")
def update_inventory(product_id: int, quantity: int, db: Session = Depends(get_db)):
    # Update inventory levels for a product and track changes over time
    inventory_item = db.query(Inventory).filter(Inventory.product_id == product_id).first()

    if inventory_item:
        # If inventory item exists, update the quantity
        inventory_item.quantity += quantity
    else:
        # If inventory item doesn't exist, create a new entry
        inventory_item = Inventory(product_id=product_id, quantity=quantity)

    # Update last_updated timestamp
    inventory_item.last_updated = datetime.now()

    # Commit changes to the database
    db.add(inventory_item)
    db.commit()

    return {"message": "Inventory updated successfully", "new_quantity": inventory_item.quantity}
