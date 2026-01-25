import pandas as pd


# ---------- Stage 1: Load Data ----------
def load_data():
    data = {
        "Company": ["A", "B", "C"],

        # Liquidity
        "CurrentAssets": [100000, 150000, 120000],
        "CurrentLiabilities": [50000, 70000, 60000],
        "Inventory": [20000, 30000, 25000],
        "Cash": [30000, 40000, 35000],

        # Leverage
        "TotalLiabilities": [80000, 110000, 90000],
        "Equity": [120000, 140000, 130000],

        # Activity
        "Sales": [200000, 280000, 240000],
        "COGS": [120000, 170000, 150000],
        "AccountsReceivable": [30000, 40000, 35000],
        "AccountsPayable": [25000, 35000, 30000],
        "TotalAssets": [200000, 250000, 220000],
    }

    df = pd.DataFrame(data)
    print("Initial data loaded:")
    print(df)
    return df


# ---------- Stage 2: Liquidity Ratios ----------
def current_ratio(df):
    df["Current_Ratio"] = df["CurrentAssets"] / df["CurrentLiabilities"]
    print("\nAfter Current Ratio:")
    print(df[["Company", "Current_Ratio"]])
    return df


def quick_ratio(df):
    df["Quick_Ratio"] = (df["CurrentAssets"] - df["Inventory"]) / df["CurrentLiabilities"]
    print("\nAfter Quick Ratio:")
    print(df[["Company", "Quick_Ratio"]])
    return df


def cash_ratio(df):
    df["Cash_Ratio"] = df["Cash"] / df["CurrentLiabilities"]
    print("\nAfter Cash Ratio:")
    print(df[["Company", "Cash_Ratio"]])
    return df


# ---------- Stage 3 & 4: Leverage Ratios ----------
def debt_to_equity_ratio(df):
    df["Debt_to_Equity"] = df["TotalLiabilities"] / df["Equity"]
    print("\nAfter Debt to Equity Ratio:")
    print(df[["Company", "Debt_to_Equity"]])
    return df


def debt_ratio(df):
    df["Debt_Ratio"] = df["TotalLiabilities"] / df["TotalAssets"]
    print("\nAfter Debt Ratio:")
    print(df[["Company", "Debt_Ratio"]])
    return df


# ---------- Stage 7: Activity Ratios ----------
def inventory_turnover(df):
    df["Inventory_Turnover"] = df["COGS"] / df["Inventory"]
    print("\nAfter Inventory Turnover:")
    print(df[["Company", "Inventory_Turnover"]])
    return df


def receivables_turnover(df):
    df["Receivables_Turnover"] = df["Sales"] / df["AccountsReceivable"]
    print("\nAfter Receivables Turnover:")
    print(df[["Company", "Receivables_Turnover"]])
    return df


def payables_turnover(df):
    df["Payables_Turnover"] = df["COGS"] / df["AccountsPayable"]
    print("\nAfter Payables Turnover:")
    print(df[["Company", "Payables_Turnover"]])
    return df


def total_asset_turnover(df):
    df["Total_Asset_Turnover"] = df["Sales"] / df["TotalAssets"]
    print("\nAfter Total Asset Turnover:")
    print(df[["Company", "Total_Asset_Turnover"]])
    return df


# ---------- Main ----------
def main():
    df = load_data()

    # Liquidity
    df = current_ratio(df)
    df = quick_ratio(df)
    df = cash_ratio(df)

    # Leverage
    df = debt_to_equity_ratio(df)
    df = debt_ratio(df)

    # Activity
    df = inventory_turnover(df)
    df = receivables_turnover(df)
    df = payables_turnover(df)
    df = total_asset_turnover(df)

    print("\nFinal DataFrame:")
    print(df)


if __name__ == "__main__":
    main()

