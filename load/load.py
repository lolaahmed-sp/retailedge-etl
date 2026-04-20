import os
import pandas as pd
import logging

def save_csv(df, filename, rows_in):
    os.makedirs('data/processed', exist_ok=True)
    path = f'data/processed/{filename}'
    df.to_csv(path, index=False)
    logging.info(f"Saved {path}")
    print(f"\n--- {filename} ---")
    print(f"  Rows in:  {rows_in}")
    print(f"  Rows out: {len(df)}")
    print(f"  Dropped:  {rows_in - len(df)}")

def load_all(customers, orders, returns, raw_counts):
    save_csv(customers, 'customers_clean.csv', raw_counts['customers'])
    save_csv(orders,    'orders_clean.csv',    raw_counts['orders'])
    save_csv(returns,   'returns_clean.csv',   raw_counts['returns'])
    print("\nPipeline complete! Cleaned files saved to data/processed/")
    