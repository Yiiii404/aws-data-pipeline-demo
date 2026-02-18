import pandas as pd

# Step 1: Extract
# Read raw data from CSV
def extract(file_path):
    df = pd.read_csv(file_path)
    return df

# Step 2: Transform
# Basic data cleaning
def transform(df):
    # Remove missing values
    df = df.dropna()
    
    # Remove duplicates
    df = df.drop_duplicates()
    
    return df

# Step 3: Load
# Save cleaned data
def load(df, output_path):
    df.to_csv(output_path, index=False)

def run_etl():
    input_file = "input.csv"
    output_file = "output.csv"
    
    df = extract(input_file)
    df_clean = transform(df)
    load(df_clean, output_file)
    
    print("ETL process completed successfully.")

if __name__ == "__main__":
    run_etl()
