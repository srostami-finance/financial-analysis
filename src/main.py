import pandas as pd


# ----------- Stage 1: Load Data -----------
def load_data(file_path):
    df = pd.read_excel(file_path)
    return df


# ----------- Stage 2: Current Ratio -----------
def current_ratio(df):
    df['Current_Ratio'] = df['CurrentAssets'] / df['CurrentLiabilities']
    return df


# ----------- Main Function -----------
def main():
    # مسیر فایل ورودی
    input_file = "../data/raw/financial_data.xlsx"

    # بارگذاری داده
    df = load_data(input_file)
    print("Initial data loaded:")
    print(df.head())

    # محاسبه Current Ratio
    df = current_ratio(df)
    print("\nAfter Current Ratio calculation:")
    print(df[['CurrentAssets', 'CurrentLiabilities', 'Current_Ratio']].head())


if __name__ == "__main__":
    main()
