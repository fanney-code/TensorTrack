import pandas as pd
import logging

def load_data(file):
    """Load data from a CSV file."""
    try:
        df = pd.read_csv(file)
        logging.info("Data loaded successfully.")
        return df
    except Exception as e:
        logging.error(f"Error loading data: {e}")
        return None

def clean_data(df):
    """Clean the dataset by handling missing values, duplicates, and outliers."""
    try:
        df.fillna(method='ffill', inplace=True)
        df.drop_duplicates(inplace=True)

        numeric_columns = df.select_dtypes(include=['number']).columns
        for column in numeric_columns:
            mean = df[column].mean()
            std_dev = df[column].std()
            df = df[(df[column] >= mean - 3 * std_dev) & (df[column] <= mean + 3 * std_dev)]

        df['date'] = pd.to_datetime(df['date'], errors='coerce')
        df.dropna(subset=['date'], inplace=True)

        logging.info("Data cleaned successfully.")
        return df
    except Exception as e:
        logging.error(f"Error cleaning data: {e}")
        return df