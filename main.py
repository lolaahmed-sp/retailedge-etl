from extract.extract import extract_all
from transform.transform import transform_customers, transform_orders, transform_returns
from load.load import load_all

def run_pipeline():
    print("Starting ETL pipeline...\n")

    # Extract
    customers, orders, returns = extract_all()
    raw_counts = {
        'customers': len(customers),
        'orders':    len(orders),
        'returns':   len(returns)
    }

    # Transform
    customers_clean = transform_customers(customers)
    orders_clean    = transform_orders(orders)
    returns_clean   = transform_returns(returns, orders_clean)

    # Load
    load_all(customers_clean, orders_clean, returns_clean, raw_counts)

if __name__ == "__main__":
    run_pipeline()
    