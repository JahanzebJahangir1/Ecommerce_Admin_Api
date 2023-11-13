# api/sales.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models.sale import Sale
from models.product import Product
from typing import List
from sqlalchemy import func
from datetime import datetime

router = APIRouter(prefix="/sales", tags=["sales"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_sales_data(
    start_date: str = None,
    end_date: str = None,
    product_id: int = None,
    category: str = None,
    db: Session = Depends(get_db)
):
    # Initialize a base query to retrieve sales data
    query = db.query(Sale)

    # Apply filters based on provided parameters
    if start_date:
        query = query.filter(Sale.sale_date >= start_date)
    if end_date:
        query = query.filter(Sale.sale_date <= end_date)
    if product_id:
        query = query.filter(Sale.product_id == product_id)
    if category:
        # Assuming a relationship between products and sales, join to filter by category
        query = query.join(Product).filter(Product.category == category)

    # Execute the query and return the sales data
    sales_data = query.all()
    return sales_data

@router.get("/revenue")
def analyze_revenue(
    start_date: str = None,
    end_date: str = None,
    period: str = "daily",
    category: str = None,
    db: Session = Depends(get_db)
):
    # Initialize a base query to calculate revenue
    query = db.query(Sale).join(Product)

    # Apply filters based on provided parameters
    if start_date:
        query = query.filter(Sale.sale_date >= start_date)
    if end_date:
        query = query.filter(Sale.sale_date <= end_date)
    if category:
        query = query.filter(Product.category == category)

    # Group by the specified period (daily, weekly, monthly, or annually)
    if period == "daily":
        query = query.group_by(Sale.sale_date)
    elif period == "weekly":
        query = query.group_by(func.week(Sale.sale_date))
    elif period == "monthly":
        query = query.group_by(func.month(Sale.sale_date))
    elif period == "annually":
        query = query.group_by(func.year(Sale.sale_date))

    # Execute the query and return the revenue analysis
    revenue_analysis = query.with_entities(
        func.sum(Sale.amount).label("total_revenue"),
        func.avg(Sale.amount).label("average_revenue")
    ).all()

    return revenue_analysis
