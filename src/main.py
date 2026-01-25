import pandas as pd

def load_data(file_path):
    df = pd.read_excel(file_path)
    print("Initial data loaded:\n", df)
    return df

# Stage 1-3: Liquidity Ratios
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

# Stage 4-6: Leverage Ratios
def add_sample_leverage_data(df):
    # اضافه کردن ستون‌های لازم برای وام، حقوق صاحبان سهام و مالیات
    df['Equity'] = [80000, 100000, 90000]
    df['TotalLiabilities'] = [50000, 70000, 60000]
    df['DebtRate'] = [0.05, 0.06, 0.055]   # نرخ بهره بدهی
    df['TaxRate'] = [0.25, 0.27, 0.26]     # نرخ مالیات
    df['FCF'] = [10000, 15000, 12000]      # جریان نقدی آزاد
    return df

def debt_to_equity_ratio(df):
    df['Debt_to_Equity'] = df['TotalLiabilities'] / df['Equity']
    print("\nAfter Debt to Equity Ratio:\n", df[['Company', 'Debt_to_Equity']])
    return df

def debt_ratio(df):
    df['Debt_Ratio'] = df['TotalLiabilities'] / (df['Equity'] + df['TotalLiabilities'])
    print("\nAfter Debt Ratio:\n", df[['Company', 'Debt_Ratio']])
    return df

# Stage 11: WACC
def calculate_wacc(df):
    df['V'] = df['Equity'] + df['TotalLiabilities']
    df['E/V'] = df['Equity'] / df['V']
    df['D/V'] = df['TotalLiabilities'] / df['V']
    df['WACC'] = df['E/V'] * 0.10 + df['D/V'] * df['DebtRate'] * (1 - df['TaxRate'])  # 0.10 = فرضی نرخ بازده حقوق صاحبان سهام
    print("\nAfter WACC Calculation:\n", df[['Company', 'WACC']])
    return df

# Stage 12: DCF Valuation
def dcf_valuation(df):
    df['DCF_Value'] = df['FCF'] / df['WACC']
    print("\nAfter DCF Valuation:\n", df[['Company', 'DCF_Value']])
    return df

def main():
    input_file = '../data/raw/financial_data.xlsx'
    df = load_data(input_file)

    # مرحله 1-3
    df = current_ratio(df)
    df = quick_ratio(df)
    df = cash_ratio(df)

    # مرحله 4-6: اضافه کردن داده‌های نمونه و محاسبه نسبت‌های بدهی
    df = add_sample_leverage_data(df)
    df = debt_to_equity_ratio(df)
    df = debt_ratio(df)

    # مرحله 11: WACC
    df = calculate_wacc(df)

    # مرحله 12: DCF
    df = dcf_valuation(df)

    # ذخیره نهایی
    df.to_excel('../data/processed/financial_ratios.xlsx', index=False)
    print("\nFinal Data Saved to processed/financial_ratios.xlsx")

if __name__ == "__main__":
    main()
