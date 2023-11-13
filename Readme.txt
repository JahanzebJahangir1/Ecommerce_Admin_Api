# E-commerce Admin API

## Setup Instructions

1. Clone the repository: `git clone https://github.com/yourusername/ecommerce_admin_api.git`

2. Change into the project directory: `cd ecommerce_admin_api`

3. Install dependencies: pip install -r requirements.txt

4. uvicorn main:app --reload

## Endpoints

## Sales

/sales/: Retrieve sales data based on filters.
/sales/revenue: Analyze revenue based on filters.

# Retrieve Sales Data:

Endpoint: /sales/
Method: GET
Parameters: start_date, end_date, product_id, category

# Analyze Revenue:

Endpoint: /sales/revenue
Method: GET
Parameters: start_date, end_date, period (daily, weekly, monthly, annually), category


## Inventory

/inventory/: View current inventory status, including low stock alerts.
/inventory/update: Update inventory levels for a product and track changes over time.

#View Current Inventory Status:

Endpoint: /inventory/
Method: GET
Parameters: low_stock_threshold (default is 10)

# Update Inventory Levels:

Endpoint: /inventory/update
Method: POST
Parameters: product_id, quantity
Demo Data
Populate Database with Demo Data:
Execute the script: python demo_data/populate_demo_data.py
