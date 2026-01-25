import pandas as pd
import os

# --- مرحله 0: فایل دیتا ---
input_file = '../data/raw/financial_data.xlsx'

# --- مرحله 1: بارگذاری داده‌ها ---
def load_data(file_path):
    if os.path.exists(file_path):
        df = pd.read_excel(file_path)
    else:
        # داده تستی اگه فایل نباشه
        df = pd.DataFrame({
            'Company': ['A', 'B', 'C'],
            'CurrentAssets': [100000, 150000, 120000],
            'CurrentLiabilities': [50000, 70000, 60000],
            'Inventory': [20000, 30000, 25000],
            'Cash': [30000, 40000, 35000],
        })
    return df

# --- مرحله 2: نسبت‌های نقدینگی ---
def current_ratio(df):
    df['Current_Ratio'] = df['CurrentAssets'] / df['CurrentLiabilities']
    print("\nAfter Current Ratio:\n", df[['Company', 'Current_Ratio']])
    return df

def quick_ratio(df):
    df['Quick_Ratio'] = (df['CurrentAssets'] - df['Inventory']) / df['CurrentLiabilities']
    print("\nAfter Quick Ratio:\n", df[['Company', 'Quick_Ratio']])
    return df

def cash_ratio(df):
    df['Cash_Ratio'] = df['Cash'] / df['CurrentLiabilities']
    print("\nAfter Cash Ratio:\n", df[['Company', 'Cash_Ratio']])
    return df

# --- مرحله 3 و 4: اضافه کردن ستون‌های بدهی و سودآوری ---
def add_missing_columns(df):
    if 'TotalLiabilities' not in df.columns:
        df['TotalLiabilities'] = [120000, 140000, 130000]
    if 'Equity' not in df.columns:
        df['Equity'] = [80000, 90000, 70000]
    if 'TotalAssets' not in df.columns:
        df['TotalAssets'] = [200000, 230000, 200000]
    if 'Revenue' not in df.columns:
        df['Revenue'] = [150000, 180000, 160000]
    if 'NetIncome' not in df.columns:
        df['NetIncome'] = [20000, 25000, 22000]
    return df

# --- مرحله 5: نسبت‌های بدهی ---
def debt_to_equity_ratio(df):
    df['Debt_to_Equity'] = df['TotalLiabilities'] / df['Equity']
    print("\nAfter Debt to Equity Ratio:\n", df[['Company', 'Debt_to_Equity']])
    return df

def debt_ratio(df):
    df['Debt_Ratio'] = df['TotalLiabilities'] / df['TotalAssets']
    print("\nAfter Debt Ratio:\n", df[['Company', 'Debt_Ratio']])
    return df

# --- مرحله 6: نسبت‌های سودآوری ---
def return_on_assets(df):
    df['ROA'] = df['NetIncome'] / df['TotalAssets']
    print("\nAfter Return on Assets (ROA):\n", df[['Company', 'ROA']])
    return df

def return_on_equity(df):
    df['ROE'] = df['NetIncome'] / df['Equity']
    print("\nAfter Return on Equity (ROE):\n", df[['Company', 'ROE']])
    return df

# --- تابع اصلی ---
def main():
    df = load_data(input_file)
    print("Initial data loaded:\n", df)

    df = add_missing_columns(df)

    df = current_ratio(df)
    df = quick_ratio(df)
    df = cash_ratio(df)

    df = debt_to_equity_ratio(df)
    df = debt_ratio(df)

    df = return_on_assets(df)
    df = return_on_equity(df)

    # خروجی نهایی
    print("\nFinal DataFrame with all ratios:\n", df)

if __name__ == "__main__":
    main()
