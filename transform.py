import pandas as pd

# def validate_df(df, required_columns):
#     if df is None:
#         print("Error: 'df' is None.")
#         return False
    
#     if not isinstance(df, pd.DataFrame):
#         print(f"Error: Expected DataFrame, but got {type(df)} instead.")
#         return False

#     missing_columns = [col for col in required_columns if col not in df.columns]
#     if missing_columns:
#         print(f"Error: Missing columns: {missing_columns}")
#         return False

#     return True

# def check_missing_data(df):
#     if validate_df(df, df.columns):
#         print("Checking for missing data...")
#         missing_data = df.isnull().sum()
#         print(missing_data)
#         return missing_data

# def check_duplicate_records(df):
#     if validate_df(df, df.columns):
#         print("\nChecking for duplicate records...")
#         duplicate_count = df.duplicated().sum()
#         duplicate_rows = df[df.duplicated()]
#         print(f"Number of duplicate rows: {duplicate_count}")
#         if duplicate_count > 0:
#             print("Duplicate rows found:")
#             print(duplicate_rows)
#         return duplicate_count, duplicate_rows

# def check_range_or_boundary(df):
#     if validate_df(df, ['Sales', 'Quantity']):
#         print("\nChecking range or boundary conditions...")
#         if df['Sales'].min() < 0:
#             print("Warning: There are negative sales values.")
#         if df['Quantity'].min() < 0:
#             print("Warning: There are negative quantities.")
#         return df

# def check_consistency(df):
#     if validate_df(df, ['Order Date', 'Ship Date']):
#         print("\nChecking consistency between Order Date and Ship Date...")
#         inconsistent_dates = df[df['Order Date'] > df['Ship Date']]
#         print(f"Inconsistent rows where Order Date > Ship Date: {len(inconsistent_dates)}")
#         if len(inconsistent_dates) > 0:
#             print(inconsistent_dates)
#         return inconsistent_dates

# def check_uniqueness(df):
#     if validate_df(df, ['Order ID', 'Row ID', 'Customer ID']):
#         print("\nChecking uniqueness of Order ID, Row ID, Customer ID...")
#         print(f"Unique Order IDs: {df['Order ID'].nunique()}")
#         print(f"Unique Row IDs: {df['Row ID'].nunique()}")
#         print(f"Unique Customer IDs: {df['Customer ID'].nunique()}")

# def check_data_types(df):
#     if validate_df(df, ['Postal Code']):
#         print("\nChecking and correcting data types...")
#         df['Postal Code'] = df['Postal Code'].astype(str)
#         print(df.dtypes)

# def check_cardinality(df):
#     if validate_df(df, ['Order ID', 'Row ID', 'Customer ID', 'Product ID', 'Ship Mode', 'Segment', 'Category', 'Postal Code']):
#         print("\nChecking cardinality of key columns...")
#         cardinalities = {
#             "Order ID": df['Order ID'].nunique(),
#             "Row ID": df['Row ID'].nunique(),
#             "Customer ID": df['Customer ID'].nunique(),
#             "Product ID": df['Product ID'].nunique(),
#             "Ship Mode": df['Ship Mode'].nunique(),
#             "Segment": df['Segment'].nunique(),
#             "Category": df['Category'].nunique(),
#             "Postal Code": df['Postal Code'].nunique(),
#         }
#         for key, value in cardinalities.items():
#             print(f"{key} Cardinality: {value}")

# def check_date_range(df):
#     if validate_df(df, ['Order Date', 'Ship Date']):
#         print("\nChecking date range for Order Date and Ship Date...")
#         print(f"Order Date range: {df['Order Date'].min()} to {df['Order Date'].max()}")
#         print(f"Ship Date range: {df['Ship Date'].min()} to {df['Ship Date'].max()}")
#         df['Days_Difference'] = (df['Ship Date'] - df['Order Date']).dt.days
#         long_shipping_times = df[df['Days_Difference'] > 365]
#         print(f"Orders with shipping times > 365 days: {len(long_shipping_times)}")
#         if len(long_shipping_times) > 0:
#             print(long_shipping_times)

# def check_profit_integrity(df):
#     if validate_df(df, ['Sales', 'Discount', 'Profit']):
#         print("\nChecking profit integrity (Profit = Sales * (1 - Discount))...")
#         df['Expected Profit'] = df['Sales'] * df['Discount']
#         profit_discrepancy = df[abs(df['Profit'] - df['Expected Profit']) > 0.01]
#         print(f"Rows with profit discrepancies: {len(profit_discrepancy)}")
#         if len(profit_discrepancy) > 0:
#             print(profit_discrepancy)

def transform_data(df):
    if validate_df(df, ['Order Date', 'Ship Date']):
        print("\nApplying transformations...")
        df['Shipping Duration'] = (df['Ship Date'] - df['Order Date']).dt.days
        df['Order Year'] = df['Order Date'].dt.year
        df['Order Month'] = df['Order Date'].dt.month
        print("Transformations applied.")
    return df
