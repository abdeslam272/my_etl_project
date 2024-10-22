import pandas as pd

def extract_data():
    """Extract data from CSV into pandas DataFrame."""
    url = 'https://raw.githubusercontent.com/abdeslam272/my_etl_project/main/data/Superstore.csv'
    df = pd.read_csv(url, encoding='ISO-8859-1')
    return df
