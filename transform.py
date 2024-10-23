import pandas as pd

def check_missing_data(df):
    if df is None:
        print("Error: 'df' is None. Cannot check for missing data.")
        return None
    
    print("Checking for missing data...")
    missing_data = df.isnull().sum()
    print(missing_data)
    return missing_data

def check_duplicate_records(df):
    if df is None:
        print("Error: 'df' is None. Cannot check for duplicate records.")
        return None, None
    
    print("\nChecking for duplicate records...")
    duplicate_count = df.duplicated().sum()
    duplicate_rows = df[df.duplicated()]
    print(f"Number of duplicate rows: {duplicate_count}")
    if duplicate_count > 0:
        print("Duplicate rows found:")
        print(duplicate_rows)
    return duplicate_count, duplicate_rows

def check_range_or_boundary(df):
    """Check the range and boundary conditions for specific columns."""
    if df is None:
        print("Error: 'df' is None. Cannot check range or boundary conditions.")
        return None
    
    # if isinstance(df, pd.DataFrame):
    #     try:
    #         print(df[['Sales', 'Quantity', 'Discount', 'Profit']].describe())
    #     except KeyError as e:
    #         print(f"Error: Missing expected columns for range check: {e}")
    #         return None
    # else:
    #     print("Error: The variable 'df' is not a DataFrame.")
    #     return None

    # Additional checks for range/boundary conditions
    if df['Sales'].min() < 0:
        print("Warning: There are negative sales values.")
    if df['Quantity'].min() < 0:
        print("Warning: There are negative quantities.")
    return df

def check_consistency(df):
    if df is None:
        print("Error: 'df' is None. Cannot check consistency.")
        return None
    
    print("\nChecking consistency between Order Date and Ship Date...")
    try:
        inconsistent_dates = df[df['Order Date'] > df['Ship Date']]
        print(f"Inconsistent rows where Order Date > Ship Date: {len(inconsistent_dates)}")
        if len(inconsistent_dates) > 0:
            print(inconsistent_dates)
        return inconsistent_dates
    except KeyError as e:
        print(f"Error: Missing expected columns for consistency check: {e}")
        return None

def check_uniqueness(df):
    if df is None:
        print("Error: 'df' is None. Cannot check uniqueness.")
        return
    
    print("\nChecking uniqueness of Order ID, Row ID, Customer ID...")
    print(f"Unique Order IDs: {df['Order ID'].nunique()}")
    print(f"Unique Row IDs: {df['Row ID'].nunique()}")
    print(f"Unique Customer IDs: {df['Customer ID'].nunique()}")

def check_data_types(df):
    if df is None:
        print("Error: 'df' is None. Cannot check data types.")
        return
    
    print("\nChecking and correcting data types...")
    df['Postal Code'] = df['Postal Code'].astype(str)
    print(df.dtypes)

def check_cardinality(df):
    if df is None:
        print("Error: 'df' is None. Cannot check cardinality.")
        return
    
    print("\nChecking cardinality of key columns...")
    cardinalities = {
        "Order ID": df['Order ID'].nunique(),
        "Row ID": df['Row ID'].nunique(),
        "Customer ID": df['Customer ID'].nunique(),
        "Product ID": df['Product ID'].nunique(),
        "Ship Mode": df['Ship Mode'].nunique(),
        "Segment": df['Segment'].nunique(),
        "Category": df['Category'].nunique(),
        "Postal Code": df['Postal Code'].nunique(),
    }
    for key, value in cardinalities.items():
        print(f"{key} Cardinality: {value}")

def check_date_range(df):
    if df is None:
        print("Error: 'df' is None. Cannot check date range.")
        return
    
    print("\nChecking date range for Order Date and Ship Date...")
    print(f"Order Date range: {df['Order Date'].min()} to {df['Order Date'].max()}")
    print(f"Ship Date range: {df['Ship Date'].min()} to {df['Ship Date'].max()}")
    df['Days_Difference'] = (df['Ship Date'] - df['Order Date']).dt.days
    long_shipping_times = df[df['Days_Difference'] > 365]
    print(f"Orders with shipping times > 365 days: {len(long_shipping_times)}")
    if len(long_shipping_times) > 0:
        print(long_shipping_times)

def check_profit_integrity(df):
    if df is None:
        print("Error: 'df' is None. Cannot check profit integrity.")
        return
    
    print("\nChecking profit integrity (Profit = Sales * (1 - Discount))...")
    df['Expected Profit'] = df['Sales'] * df['Discount']
    profit_discrepancy = df[abs(df['Profit'] - df['Expected Profit']) > 0.01]
    print(f"Rows with profit discrepancies: {len(profit_discrepancy)}")
    if len(profit_discrepancy) > 0:
        print(profit_discrepancy)

def check_categories(df):
    if df is None:
        print("Error: 'df' is None. Cannot check categories.")
        return
    
    print("\nChecking categories for Ship Mode and Segment...")
    expected_ship_modes = ['Standard Class', 'Second Class', 'First Class', 'Same Day']
    unique_ship_modes = df['Ship Mode'].unique()
    unexpected_ship_modes = set(unique_ship_modes) - set(expected_ship_modes)
    print(f"Unexpected Ship Modes: {unexpected_ship_modes}")

    expected_segments = ['Consumer', 'Corporate', 'Home Office']
    unique_segments = df['Segment'].unique()
    unexpected_segments = set(unique_segments) - set(expected_segments)
    print(f"Unexpected Segments: {unexpected_segments}")

def transform_data(df):
    if df is None:
        print("Error: 'df' is None. Cannot apply transformations.")
        return df
    
    print("\nApplying transformations...")
    df['Shipping Duration'] = (df['Ship Date'] - df['Order Date']).dt.days
    df['Order Year'] = df['Order Date'].dt.year
    df['Order Month'] = df['Order Date'].dt.month
    print("Transformations applied.")
    return df
