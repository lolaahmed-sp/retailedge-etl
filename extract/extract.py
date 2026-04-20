import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)

REQUIRED_CUSTOMERS = ['customer_id', 'name', 'email', 'signup_date']
REQUIRED_ORDERS    = ['order_id', 'customer_id', 'order_date', 'amount', 'product_category']
REQUIRED_RETURNS   = ['return_id', 'order_id', 'return_date']

def load_csv(path, required_cols):
    df = pd.read_csv(path)
    logging.info(f"Loaded {path}: {len(df)} rows")
    missing = [c for c in required_cols if c not in df.columns]
    if missing:
        logging.warning(f"Missing columns in {path}: {missing}")
    return df

def extract_all():
    customers = load_csv('data/raw/customers_large.csv', REQUIRED_CUSTOMERS)
    orders    = load_csv('data/raw/orders_large.csv',    REQUIRED_ORDERS)
    returns   = load_csv('data/raw/returns_large.csv',   REQUIRED_RETURNS)
    return customers, orders, returns