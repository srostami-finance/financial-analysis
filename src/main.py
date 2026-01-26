# main.py
import pandas as pd
import numpy as np
import statsmodels.api as sm
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier
import os

# ------------------------------
# Stage 0 → Load Data
# ------------------------------
def load_data(file_path):
    if not os.path.exists(file_path):
        # اگر فایل موجود نبود، داده نمونه بساز
        df = pd.DataFrame({
            'Company': ['A','B','C'],
            'CurrentAssets':[100000,150000,120000],
            'CurrentLiabilities':[50000,70000,60000],
            'Inventory':[20000,30000,25000],
            'Cash':[30000,40000,35000]
        })
        print("Sample data created.\n")
    else:
        df = pd.read_excel(file_path)
        print("Initial data loaded:\n", df.head())
    return df

# ------------------------------
# Stage 1 → Liquidity Ratios
# ------------------------------
def current_ratio(df):
    df['Current_Ratio'] = df['CurrentAssets'] / df['CurrentLiabilities']
    print("\nAfter Current Ratio:")
    print(df[['Company','Current_Ratio']])
    return df

def quick_ratio(df):
    df['Quick_Ratio'] = (df['CurrentAssets'] - df['Inventory']) / df['CurrentLiabilities']
    print("\nAfter Quick Ratio:")
    print(df[['Company','Quick_Ratio']])
    return df

def cash_ratio(df):
    df['Cash_Ratio'] = df['Cash'] / df['CurrentLiabilities']
    print("\nAfter Cash Ratio:")
    print(df[['Company','Cash_Ratio']])
    return df

# ------------------------------
# Stage 2 → Solvency Ratios
# ------------------------------
def debt_to_equity_ratio(df):
    # اضافه کردن ستون نمونه اگر موجود نیست
    if 'Equity' not in df.columns:
        df['Equity'] = [50000,80000,60000]
    if 'TotalLiabilities' not in df.columns:
        df['TotalLiabilities'] = [50000,70000,60000]

    df['Debt_to_Equity'] = df['TotalLiabilities'] / df['Equity']
    print("\nAfter Debt to Equity Ratio:")
    print(df[['Company','Debt_to_Equity']])
    return df

def debt_ratio(df):
    df['Debt_Ratio'] = df['TotalLiabilities'] / (df['Equity'] + df['TotalLiabilities'])
    print("\nAfter Debt Ratio:")
    print(df[['Company','Debt_Ratio']])
    return df

# ------------------------------
# Stage 3 → CAPM
# ------------------------------
def capm_expected_return(df, risk_free=0.03, market_return=0.1):
    beta_example = [1.0, 0.8, 0.9]
    df['Expected_Return'] = risk_free + np.array(beta_example)*(market_return - risk_free)
    print("\nAfter CAPM:")
    print(df[['Company','Expected_Return']])
    return df

# ------------------------------
# Stage 4 → WACC
# ------------------------------
def calculate_wacc(df, debt_rate=0.05):
    if 'Equity' not in df.columns:
        df['Equity'] = [50000,80000,60000]
    if 'TotalLiabilities' not in df.columns:
        df['TotalLiabilities'] = [50000,70000,60000]
    df['V'] = df['Equity'] + df['TotalLiabilities']
    df['E/V'] = df['Equity'] / df['V']
    df['D/V'] = df['TotalLiabilities'] / df['V']
    df['WACC'] = df['E/V'] * df['Expected_Return'] + df['D/V'] * debt_rate * (1-0.25)
    print("\nAfter WACC:")
    print(df[['Company','WACC']])
    return df

# ------------------------------
# Stage 5 → DCF Valuation
# ------------------------------
def dcf_valuation(df, growth_rate=0.05):
    # ایجاد ستون FreeCashFlow نمونه
    if 'FCF' not in df.columns:
        df['FCF'] = [5000,7000,6000]
    df['DCF_Value'] = df['FCF'] / (df['WACC'] - growth_rate)
    print("\nAfter DCF Valuation:")
    print(df[['Company','DCF_Value']])
    return df

# ------------------------------
# Stage 6 → Fama-French Regression
# ------------------------------
def fama_french_regression(df):
    # داده نمونه فاکتورهای SMB و HML
    df['SMB'] = [0.05,0.05,0.05]
    df['HML'] = [0.02,0.02,0.02]
    X = df[['Expected_Return','SMB','HML']]
    X = sm.add_constant(X, has_constant='add')  # اضافه کردن ستون ثابت
    y = df['Expected_Return']
    model = sm.OLS(y, X).fit()

    # بررسی وجود ستون ثابت
    if 'const' in model.params.index:
        df['Alpha'] = model.params['const']
    else:
        df['Alpha'] = 0.0

    df['Beta_Market'] = model.params.get('Expected_Return', 0.0)
    df['Beta_SMB'] = model.params.get('SMB', 0.0)
    df['Beta_HML'] = model.params.get('HML', 0.0)

    print("\nAfter Fama-French Regression:")
    print(df[['Company','Alpha','Beta_Market','Beta_SMB','Beta_HML']])
    return df

# ------------------------------
# Stage 7 → ML Financial Distress Prediction
# ------------------------------
def ml_financial_distress(df):
    # اضافه کردن ستون نمونه نسبت های مالی برای ML
    features = ['Current_Ratio','Quick_Ratio','Cash_Ratio','Debt_to_Equity','Debt_Ratio']
    X = df[features]
    # ستون نمونه هدف: 0 و 1
    if 'Distress' not in df.columns:
        df['Distress'] = [0,1,0]  # داده نمونه با حداقل 2 کلاس
    y = df['Distress']

    # Logistic Regression
    logreg = LogisticRegression()
    logreg.fit(X, y)
    df['Distress_LogReg_Pred'] = logreg.predict(X)

    # Neural Network
    nn = MLPClassifier(hidden_layer_sizes=(5,), max_iter=500)
    nn.fit(X, y)
    df['Distress_NN_Pred'] = nn.predict(X)

    print("\nAfter ML Financial Distress Prediction:")
    print(df[['Company','Distress_LogReg_Pred','Distress_NN_Pred']])
    return df

# ------------------------------
# Main
# ------------------------------
def main():
    input_file = '../data/financial_data.xlsx'
    output_file = '../data/processed/financial_analysis_results.xlsx'

    df = load_data(input_file)

    # مرحله به مرحله
    df = current_ratio(df)
    df = quick_ratio(df)
    df = cash_ratio(df)
    df = debt_to_equity_ratio(df)
    df = debt_ratio(df)
    df = capm_expected_return(df)
    df = calculate_wacc(df)
    df = dcf_valuation(df)
    df = fama_french_regression(df)
    df = ml_financial_distress(df)

    # ذخیره نهایی
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    df.to_excel(output_file, index=False)
    print(f"\nFinal processed data saved to {output_file}")

if __name__ == "__main__":
    main()

