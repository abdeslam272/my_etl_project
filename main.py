from extract import extract_data
from transform import check_missing_data,check_duplicate_records,..., transform_data
from load import load_data, save_data

def main():
    # Step 1: Extract
    df = extract_data()

    # Step 2: Transform
    df = data_quality_checks(df)
    df = transform_data(df)

    # Step 3: Load
    db_path = 'data/dim_customer.sqlite'
    load(df, db_path)


if __name__ == '__main__':
    main()
