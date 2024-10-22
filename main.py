from extract import extract_data
from transform import check_missing_data, check_duplicate_records, check_range_or_boundary, check_consistency, check_uniqueness, check_data_types, check_cardinality, check_date_range, check_profit_integrity, check_categories, transform_data
from load import load_data, save_data

def main():
    # Step 1: Extract
    df = extract_data()

    # Step 2: Transform
    if df is not None:
        df = check_missing_data(df)
        df = check_duplicate_records(df)
        df = check_range_or_boundary(df)
        df = check_consistency(df)
        df = check_uniqueness(df)
        df = check_data_types(df)
        df = check_cardinality(df)
        df = check_date_range(df)
        df = check_profit_integrity(df)
        df = check_categories(df)

        df = transform_data(df)

    # Step 3: Load
    dim_customer, dim_time, fact_sales = load_data()

    save_data(dim_customer, dim_time, fact_sales)


if __name__ == '__main__':
    main()
