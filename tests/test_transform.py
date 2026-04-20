import pandas as pd
import pytest
from transform.transform import transform_customers, transform_orders, transform_returns

def test_customers_drops_missing_name():
    df = pd.DataFrame({
        'customer_id': [1, 2, 3],
        'name': ['Alice', None, 'Bob'],
        'signup_date': ['2024-01-01', '2024-01-02', '2024-01-03']
    })
    result = transform_customers(df)
    assert len(result) == 2

def test_customers_trims_whitespace():
    df = pd.DataFrame({
        'customer_id': [1],
        'name': ['  Alice  '],
        'signup_date': ['2024-01-01']
    })
    result = transform_customers(df)
    assert result.iloc[0]['name'] == 'Alice'

def test_customers_removes_duplicates():
    df = pd.DataFrame({
        'customer_id': [1, 1],
        'name': ['Alice', 'Alice'],
        'signup_date': ['2024-01-01', '2024-01-01']
    })
    result = transform_customers(df)
    assert len(result) == 1

def test_orders_normalises_category():
    df = pd.DataFrame({
        'order_id': [1],
        'customer_id': [1],
        'order_date': ['2024-01-01'],
        'amount': [50],
        'product_category': ['Home Goods']
    })
    result = transform_orders(df)
    assert result.iloc[0]['product_category'] == 'home_goods'

def test_orders_drops_invalid_dates():
    df = pd.DataFrame({
        'order_id': [1, 2],
        'customer_id': [1, 2],
        'order_date': ['2024-01-01', 'not-a-date'],
        'amount': [50, 30],
        'product_category': ['electronics', 'books']
    })
    result = transform_orders(df)
    assert len(result) == 1

def test_orders_converts_amount_to_float():
    df = pd.DataFrame({
        'order_id': [1],
        'customer_id': [1],
        'order_date': ['2024-01-01'],
        'amount': ['99.99'],
        'product_category': ['books']
    })
    result = transform_orders(df)
    assert result.iloc[0]['amount'] == 99.99

def test_returns_removes_invalid_order_ids():
    orders_df = pd.DataFrame({
        'order_id': [1, 2],
        'customer_id': [1, 2],
        'order_date': ['2024-01-01', '2024-01-02'],
        'amount': [50, 30],
        'product_category': ['books', 'electronics']
    })
    returns_df = pd.DataFrame({
        'order_id': [1, 99],
        'return_date': ['2024-02-01', '2024-02-02']
    })
    result = transform_returns(returns_df, orders_df)
    assert len(result) == 1
    assert result.iloc[0]['order_id'] == 1
    