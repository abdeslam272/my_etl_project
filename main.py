from extract import extract_data
from transform import transform_data
# (
#     check_missing_data, check_duplicate_records, check_range_or_boundary,
#     check_consistency, check_uniqueness, check_data_types, check_cardinality,
#     check_date_range, check_profit_integrity, check_categories, transform_data
# )
from load import load_data, save_data

def main():
    # Step 1: Extract Data (assuming extract_data() retrieves data from a source)
    print("Extracting data...")
    df = extract_data()  # Ensure that extract_data() returns a valid DataFrame

    # Step 2: Perform quality checks
    print("\nPerforming quality checks...")
    # check_missing_data(df)
    # check_duplicate_records(df)
    # check_range_or_boundary(df)
    # check_consistency(df)
    # check_uniqueness(df)
    # check_data_types(df)
    # check_cardinality(df)
    # check_date_range(df)
    # check_profit_integrity(df)
    # check_categories(df)

    # Step 3: Apply transformations
    print("\nApplying transformations...")
    transformed_df = transform_data(df)

    # Step 4: Return or save the transformed DataFrame
    print("\nTransformed data:")
    print(transformed_df.head())  # Print the first few rows of the transformed DataFrame

    # If you want to save the transformed DataFrame to a file (optional)
    transformed_df.to_csv('transformed_data.csv', index=False)
    print("\nTransformed data saved to 'transformed_data.csv'.")

    # Step 3: Load
    dim_customer, dim_time, fact_sales = load_data(transformed_df)

    save_data(dim_customer, dim_time, fact_sales)


if __name__ == '__main__':
    main()
