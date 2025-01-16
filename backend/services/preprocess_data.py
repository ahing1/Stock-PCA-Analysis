import os
import pandas as pd
from sklearn.preprocessing import StandardScaler

DATA_DIR = "./data/raw"
PROCESSED_DATA_DIR = "./data/processed"

os.makedirs(PROCESSED_DATA_DIR, exist_ok=True)

def load_data(file_path):
    """Load raw stock data."""
    return pd.read_csv(file_path)

def handle_missing_values(df):
    """
    Handle missing data by interpolation for numeric columns only.
    Non-numeric columns are left unchanged.
    """
    # Identify numeric columns
    numeric_cols = df.select_dtypes(include=['number']).columns

    # Interpolate only numeric columns
    df[numeric_cols] = df[numeric_cols].interpolate(method='linear', axis=0)

    # Drop rows or columns where all values are still missing
    df = df.dropna(how='all', axis=1)  # Drop columns with all NaN
    df = df.dropna(how='all', axis=0)  # Drop rows with all NaN

    return df

def normalize_data(df):
    """Normalize numeric features using StandardScaler."""
    numeric_data = df.select_dtypes(include=['number'])

    # Drop columns with all NaN values (if any)
    numeric_data = numeric_data.dropna(how='all', axis=1)

    # Fill remaining NaN values with a placeholder (e.g., the column mean)
    numeric_data = numeric_data.fillna(numeric_data.mean())

    # Normalize the numeric data
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(numeric_data)
    df[numeric_data.columns] = scaled_data
    return df


def remove_unnecessary_columns(df):
    """Remove redundant or unnecessary columns."""
    return df.drop(columns=['Adj Close'], errors='ignore')

def preprocess_file(file_path):
    """Full preprocessing pipeline for a single file."""
    print(f"Processing {file_path}...")
    df = load_data(file_path)

    # Convert all columns to numeric where applicable
    for column in df.columns:
        if column not in ['Date']:  # Exclude non-numeric columns like Date
            df[column] = pd.to_numeric(df[column], errors='coerce')

    # Handle missing values and normalize data
    df = handle_missing_values(df)
    df = normalize_data(df)
    return df


def main():
    """Process all files in the raw data directory."""
    for file_name in os.listdir(DATA_DIR):
        raw_file_path = os.path.join(DATA_DIR, file_name)
        
        # Check if the current path is a file and ends with .csv
        if os.path.isfile(raw_file_path) and file_name.endswith('.csv'):
            processed_file_path = os.path.join(PROCESSED_DATA_DIR, file_name)

            # Process the file
            df = preprocess_file(raw_file_path)
            df.to_csv(processed_file_path, index=False)
            print(f"Processed data saved to {processed_file_path}")


if __name__ == "__main__":
    main()