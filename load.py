# load.py
import os
import pandas as pd

def load_data(transformed_df):
    # Use the transformed DataFrame directly instead of reading from CSV
    Superstore = transformed_df

    # 1. Create the Dimensional and Fact tables

    # dim_customer: Contains customer information
    dim_customer = Superstore[['Customer ID', 'Customer Name', 'Segment', 'Country', 'City', 'Postal Code', 'Region']].drop_duplicates()

    # dim_time: Contains the date information
    dim_time = Superstore[['Order Date']].drop_duplicates()
#    dim_time = Superstore[['Order Date', 'Order Year', 'Order Month']].drop_duplicates()

    # fact_sales: Contains sales-related metrics
#    fact_sales = Superstore[['Order ID', 'Product ID', 'Sales', 'Quantity', 'Discount', 'Profit', 'Shipping Duration']]
    fact_sales = Superstore[['Order ID', 'Product ID', 'Sales', 'Quantity', 'Discount', 'Profit']]

    return dim_customer, dim_time, fact_sales

def save_data(dim_customer, dim_time, fact_sales):
    # Ensure 'data/' directory exists
    if not os.path.exists('data'):
        os.makedirs('data')

    # Save dim_customer
    dim_customer.to_csv('data/dim_customer.csv', index=False)
    print("dim_customer.csv saved successfully.")

    # Save dim_time
    dim_time.to_csv('data/dim_time.csv', index=False)
    print("dim_time.csv saved successfully.")

    # Save fact_sales
    fact_sales.to_csv('data/fact_sales.csv', index=False)
    print("fact_sales.csv saved successfully.")
