import pandas as pd
import logging

def transform_customers(df):
    rows_in = len(df)
    df = df.copy()
    df['name'] = df['name'].str.strip()
    df['signup_date'] = pd.to_datetime(df['signup_date'], errors='coerce')
    df = df.dropna(subset=['customer_id', 'name'])
    df = df.drop_duplicates()
    logging.info(f"Customers: {rows_in} in → {len(df)} out | dropped {rows_in - len(df)} rows")
    return df

def transform_orders(df):
    rows_in = len(df)
    df = df.copy()
    df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
    invalid_dates = df['order_date'].isna().sum()
    if invalid_dates > 0:
        logging.warning(f"Dropping {invalid_dates} rows with invalid order_date")
    df = df[df['order_date'].notna()]
    df['amount'] = pd.to_numeric(df['amount'], errors='coerce')
    df = df.dropna(subset=['order_id', 'customer_id'])
    df['product_category'] = (df['product_category']
                               .str.lower()
                               .str.strip()
                               .str.replace(' ', '_', regex=False))
    logging.info(f"Orders: {rows_in} in → {len(df)} out | dropped {rows_in - len(df)} rows")
    return df

def transform_returns(df, orders_df):
    rows_in = len(df)
    df = df.copy()
    valid_orders = set(orders_df['order_id'])
    df = df[df['order_id'].isin(valid_orders)]
    df['return_date'] = pd.to_datetime(df['return_date'], errors='coerce')
    logging.info(f"Returns: {rows_in} in → {len(df)} out | dropped {rows_in - len(df)} rows")
    return df
