import pandas as pd
import numpy as np
import statsmodels.api as sm
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier


# -------------------------------
# Stage 1: Load Data
# -------------------------------
def load_data(file_path):
    try:
        df = pd.read_excel(file_path)
        print("Initial data loaded:\n", df.head())
    except FileNotFoundError:
        # نمونه داده اگر فایل موجود نباشد
        df = pd.DataFrame({
            'Company': ['A', 'B', 'C'],
            'CurrentAssets': [100000, 150000, 120000],
            'CurrentLiabilities': [50000, 70000, 60000],
            'Inventory': [20000, 30000, 25000],
            'Cash': [30000, 40000, 35000]
        })
        print("Sample data created:\n", df.head())
    return df


# -------------------------------
# Stage 2-3: Liquidity Ratios
# -------------------------------
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


# -------------------------------
# Stage 4-5: Leverage Ratios
# -------------------------------
def debt_to_equity_ratio(df):
    if 'TotalLiabilities' not in df.columns:
        df['TotalLiabilities'] = [50000, 56000, 60000]
    if 'Equity' not in df.columns:
        df['Equity'] = [50000, 64000, 60000]
    df['Debt_to_Equity'] = df['TotalLiabilities'] / df['Equity']
    print("\nAfter Debt to Equity Ratio:\n", df[['Company', 'Debt_to_Equity']])
    return df


def debt_ratio(df):
    if 'TotalLiabilities' not in df.columns:
        df['TotalLiabilities'] = [50000, 56000, 60000]
    if 'Equity' not in df.columns:
        df['Equity'] = [50000, 64000, 60000]
    df['Debt_Ratio'] = df['TotalLiabilities'] / (df['Equity'] + df['TotalLiabilities'])
    print("\nAfter Debt Ratio:\n", df[['Company', 'Debt_Ratio']])
    return df


# -------------------------------
# Stage 11: WACC
# -------------------------------
def calculate_wacc(df):
    if 'TotalLiabilities' not in df.columns:
        df['TotalLiabilities'] = [50000, 56000, 60000]
    if 'Equity' not in df.columns:
        df['Equity'] = [50000, 64000, 60000]
    df['Cost_of_Debt'] = [0.05, 0.04, 0.045]
    df['Cost_of_Equity'] = [0.10, 0.09, 0.095]
    df['Tax_Rate'] = [0.2, 0.2, 0.2]
    df['V'] = df['Equity'] + df['TotalLiabilities']
    df['WACC'] = (df['Equity'] / df['V']) * df['Cost_of_Equity'] + (df['TotalLiabilities'] / df['V']) * df[
        'Cost_of_Debt'] * (1 - df['Tax_Rate'])
    print("\nAfter WACC:\n", df[['Company', 'WACC']])
    return df


# -------------------------------
# Stage 12: DCF Valuation
# -------------------------------
def dcf_valuation(df):
    if 'CashFlow' not in df.columns:
        df['CashFlow'] = [10000, 15000, 12000]
    if 'WACC' not in df.columns:
        df['WACC'] = [0.08, 0.07, 0.075]
    df['DCF_Value'] = df['CashFlow'] / df['WACC']
    print("\nAfter DCF Valuation:\n", df[['Company', 'DCF_Value']])
    return df


# -------------------------------
# Stage 8: CAPM Expected Return
# -------------------------------
def capm(df):
    if 'Beta' not in df.columns:
        df['Beta'] = [1.2, 0.9, 1.0]
    Rf = 0.03
    Rm = 0.10
    df['Expected_Return'] = Rf + df['Beta'] * (Rm - Rf)
    print("\nAfter CAPM:\n", df[['Company', 'Expected_Return']])
    return df


# -------------------------------
# Stage 13: Fama-French Regression
# -------------------------------
def fama_french_regression(df):
    if 'Excess_Return' not in df.columns:
        df['Excess_Return'] = df['Expected_Return'] - 0.03
    df['SMB'] = [0.02, 0.015, 0.018]
    df['HML'] = [0.01, 0.02, 0.015]
    df['Market_Excess'] = df['Expected_Return'] - 0.03
    X = df[['Market_Excess', 'SMB', 'HML']]
    X = sm.add_constant(X)
    y = df['Excess_Return']
    model = sm.OLS(y, X).fit()
    df['Alpha'] = model.params.get('const', 0)
    df['Beta_Market'] = model.params.get('Market_Excess', 0)
    df['Beta_SMB'] = model.params.get('SMB', 0)
    df['Beta_HML'] = model.params.get('HML', 0)
    print("\nAfter Fama-French Regression:\n", df[['Company', 'Alpha', 'Beta_Market', 'Beta_SMB', 'Beta_HML']])
    return df


# -------------------------------
# Stage 14: ML Financial Distress Prediction
# -------------------------------
def financial_distress_ml(df):
    # ستون های نمونه برای الگوریتم ML
    features = ['Current_Ratio', 'Quick_Ratio', 'Cash_Ratio', 'Debt_to_Equity', 'Debt_Ratio']
    for f in features:
        if f not in df.columns:
            df[f] = 1.0  # عدد فرضی برای پر کردن

    # ستون هدف نمونه
    if 'Distress' not in df.columns:
        df['Distress'] = [0, 1, 0]  # 1 = شرکت در بحران مالی، 0 = سالم

    X = df[features]
    y = df['Distress']

    # Logistic Regression
    logreg = LogisticRegression()
    logreg.fit(X, y)
    df['Distress_LogReg_Pred'] = logreg.predict(X)

    # Neural Network
    nn = MLPClassifier(hidden_layer_sizes=(5,), max_iter=500, random_state=42)
    nn.fit(X, y)
    df['Distress_NN_Pred'] = nn.predict(X)

    print("\nAfter ML Financial Distress Prediction:\n", df[['Company', 'Distress_LogReg_Pred', 'Distress_NN_Pred']])
    return df


# -------------------------------
# Main
# -------------------------------
def main():
    input_file = '../data/raw/financial_data.xlsx'
    df = load_data(input_file)
    df = current_ratio(df)
    df = quick_ratio(df)
    df = cash_ratio(df)
    df = debt_to_equity_ratio(df)
    df = debt_ratio(df)
    df = calculate_wacc(df)
    df = dcf_valuation(df)
    df = capm(df)
    df = fama_french_regression(df)
    df = financial_distress_ml(df)

    df.to_excel('../data/processed/financial_analysis_results.xlsx', index=False)
    print("\nFinal processed data saved to ../data/processed/financial_analysis_results.xlsx")


if __name__ == "__main__":
    main()
