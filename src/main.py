import pandas as pd

def load_data(file_path):
    df = pd.read_excel(file_path)
    return df

def main():
    input_file = "../data/raw/financial_data.xlsx"
    df = load_data(input_file)
    print(df.head())

if __name__ == "__main__":
    main()

