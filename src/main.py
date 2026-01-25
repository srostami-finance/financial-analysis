import pandas as pd


# ----------- Stage 1: Load Data -----------
def load_data(file_path):
    try:
        df = pd.read_excel(file_path)
        return df
    except FileNotFoundError:
        raise FileNotFoundError(f"{file_path} not found.")


# ----------- Stage 2: Current Ratio -----------
def current_ratio(df):
    df['Current_Ratio'] = df['CurrentAssets'] / df['CurrentLiabilities']
    return df


# ----------- Stage 3: Quick Ratio -----------
def quick_ratio(df):
    df['Quick_Ratio'] = (df['CurrentAssets'] - df['Inventory']) / df['CurrentLiabilities']
    return df


# ---------- Main Function ----------
def main():
    input_file = "../data/raw/financial_data.xlsx"

    # Stage 1: Load Data
    df = load_data(input_file)
    print("Initial data loaded:")
    print(df.head())

    # Stage 2: Current Ratio
    df = current_ratio(df)
    print("\nAfter Current Ratio calculation:")
    print(df[['CurrentAssets', 'CurrentLiabilities', 'Current_Ratio']].head())

    # Stage 3: Quick Ratio
    df = quick_ratio(df)
    print("\nAfter Quick Ratio calculation:")
    print(df[['CurrentAssets', 'Inventory', 'CurrentLiabilities', 'Quick_Ratio']].head())


if __name__ == "__main__":
    main()
