# src/main.py
import pandas as pd

# ================================
# Stage 0: Load initial data
# ================================
def load_data():
    # داده‌های تستی برای سه شرکت
    df = pd.DataFrame({
        'Company': ['A', 'B', 'C'],
        'CurrentAssets': [100000, 150000, 120000],
        'CurrentLiabilities': [50000, 70000, 60000],
        'Inventory': [20000, 30000, 25000],
        'Cash': [30000, 40000, 35000],
        'TotalLiabilities': [80000, 100000, 90000],
        'Equity': [70000, 120000, 90000],
        'NetIncome': [10000, 20000, 15000],
        'Revenue': [50000, 70000, 60000],
        'NOPAT': [8000, 15000, 12000]
    })
    print("Initial data loaded:\n", df, "\n")
    return df

# ================================
# Stage 1-3: Liquidity Ratios
# ================================
def current_ratio(df):
    df['Current_Ratio'] = df['CurrentAssets'] / df['CurrentLiabilities']
    print("After Current Ratio:\n", df[['Company','Current_Ratio']], "\n")
    return df

def quick_ratio(df):
    df['Quick_Ratio'] = (df['CurrentAssets'] - df['Inventory']) / df['CurrentLiabilities']
    print("After Quick Ratio:\n", df[['Company','Quick_Ratio']], "\n")
    return df

def cash_ratio(df):
    df['Cash_Ratio'] = df['Cash'] / df['CurrentLiabilities']
    print("After Cash Ratio:\n", df[['Company','Cash_Ratio']], "\n")
    return df

# ================================
# Stage 4-6: Leverage Ratios
# ================================
def debt_to_equity_ratio(df):
    df['Debt_to_Equity'] = df['TotalLiabilities'] / df['Equity']
    print("After Debt to Equity Ratio:\n", df[['Company','Debt_to_Equity']], "\n")
    return df

def debt_ratio(df):
    df['Debt_Ratio'] = df['TotalLiabilities'] / (df['TotalLiabilities'] + df['Equity'])
    print("After Debt Ratio:\n", df[['Company','Debt_Ratio']], "\n")
    return df

# ================================
# Stage 7-8: Profitability Ratios
# ================================
def roe(df):
    df['ROE'] = df['NetIncome'] / df['Equity']
    print("After ROE:\n", df[['Company','ROE']], "\n")
    return df

def roa(df):
    df['ROA'] = df['NetIncome'] / (df['TotalLiabilities'] + df['Equity'])
    print("After ROA:\n", df[['Company','ROA']], "\n")
    return df

# ================================
# Stage 9-10: Efficiency Ratios
# ================================
def net_profit_margin(df):
    df['Net_Profit_Margin'] = df['NetIncome'] / df['Revenue']
    print("After Net Profit Margin:\n", df[['Company','Net_Profit_Margin']], "\n")
    return df

def return_on_capital(df):
    df['ROIC'] = df['NOPAT'] / (df['TotalLiabilities'] + df['Equity'])
    print("After ROIC:\n", df[['Company','ROIC']], "\n")
    return df

# ================================
# Stage 11: WACC
# ================================
def wacc(df, equity_cost=0.12, debt_cost=0.06, tax_rate=0.25):
    # WACC = E/V * Re + D/V * Rd * (1 - Tc)
    df['Total_Capital'] = df['TotalLiabilities'] + df['Equity']
    df['WACC'] = (df['Equity']/df['Total_Capital'])*equity_cost + \
                 (df['TotalLiabilities']/df['Total_Capital'])*debt_cost*(1-tax_rate)
    print("After WACC:\n", df[['Company','WACC']], "\n")
    return df

# ================================
# Main function
# ================================
def main():
    df = load_data()

    # Liquidity
    df = current_ratio(df)
    df = quick_ratio(df)
    df = cash_ratio(df)

    # Leverage
    df = debt_to_equity_ratio(df)
    df = debt_ratio(df)

    # Profitability
    df = roe(df)
    df = roa(df)

    # Efficiency
    df = net_profit_margin(df)
    df = return_on_capital(df)

    # WACC
    df = wacc(df)

    # Final
    print("Final DataFrame with all ratios:\n", df)

if __name__ == "__main__":
    main()
