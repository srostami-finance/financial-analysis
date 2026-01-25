# src/main.py
import pandas as pd


# ----------- Stage 1: Load Data -----------
def load_data(file_path):
    try:
        df = pd.read_excel(file_path)
        print("Initial data loaded:")
        print(df.head())
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


# ----------- Stage 4: Cash Ratio -----------
def cash_ratio(df):
    df['Cash_Ratio'] = df['Cash'] / df['CurrentLiabilities']
    return df


# ----------- Main Function -----------
def main():
    input_file = "../data/raw/financial_data.xlsx"

    # Stage 1
    df = load_data(input_file)

    # Stage 2
    df = current_ratio(df)
    print("\nAfter Current Ratio calculation:")
    print(df[['CurrentAssets', 'CurrentLiabilities', 'Current_Ratio']].head())

    # Stage 3
    df = quick_ratio(df)
    print("\nAfter Quick Ratio calculation:")
    print(df[['CurrentAssets', 'Inventory', 'CurrentLiabilities', 'Quick_Ratio']].head())

    # Stage 4
    df = cash_ratio(df)
    print("\nAfter Cash Ratio calculation:")
    print(df[['Cash', 'CurrentLiabilities', 'Cash_Ratio']].head())

    # Optionally save the results
    output_file = "../data/processed/financial_ratios.xlsx"
    df.to_excel(output_file, index=False)
    print(f"\nResults saved to {output_file}")


# ----------- Run the script -----------
if __name__ == "__main__":
    main()
