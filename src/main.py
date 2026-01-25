# src/main.py
import pandas as pd
import os


def load_data(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_path} not found.")
    df = pd.read_excel(file_path)
    print("Initial data loaded:")
    print(df.head())
    return df


# مرحله 1: Current Ratio
def current_ratio(df):
    df['Current_Ratio'] = df['CurrentAssets'] / df['CurrentLiabilities']
    print("\nAfter Current Ratio:")
    print(df[['Company', 'Current_Ratio']])
    return df


# مرحله 2: Quick Ratio
def quick_ratio(df):
    df['Quick_Ratio'] = (df['CurrentAssets'] - df['Inventory']) / df['CurrentLiabilities']
    print("\nAfter Quick Ratio:")
    print(df[['Company', 'Quick_Ratio']])
    return df


# مرحله 3: Cash Ratio
def cash_ratio(df):
    df['Cash_Ratio'] = df['Cash'] / df['CurrentLiabilities']
    print("\nAfter Cash Ratio:")
    print(df[['Company', 'Cash_Ratio']])
    return df


# مرحله 4: Working Capital
def working_capital(df):
    df['Working_Capital'] = df['CurrentAssets'] - df['CurrentLiabilities']
    print("\nAfter Working Capital:")
    print(df[['Company', 'Working_Capital']])
    return df


# مرحله 5: Debt-to-Equity Ratio
def debt_to_equity_ratio(df):
    # اگر ستون‌ها وجود ندارند، مقادیر فرضی اضافه می‌کنیم
    if 'TotalLiabilities' not in df.columns:
        df['TotalLiabilities'] = [120000, 140000, 130000]
    if 'Equity' not in df.columns:
        df['Equity'] = [80000, 90000, 85000]
    df['Debt_to_Equity'] = df['TotalLiabilities'] / df['Equity']
    print("\nAfter Debt-to-Equity Ratio:")
    print(df[['Company', 'Debt_to_Equity']])
    return df


def main():
    input_file = "../data/raw/financial_data.xlsx"
    df = load_data(input_file)

    df = current_ratio(df)
    df = quick_ratio(df)
    df = cash_ratio(df)
    df = working_capital(df)
    df = debt_to_equity_ratio(df)


if __name__ == "__main__":
    main()
