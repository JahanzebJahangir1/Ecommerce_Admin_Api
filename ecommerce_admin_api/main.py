from fastapi import FastAPI
from api import products, sales, inventory

app = FastAPI()

app.include_router(products.router)
app.include_router(sales.router)
app.include_router(inventory.router)