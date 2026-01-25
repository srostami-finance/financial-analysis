import pandas as pd


def load_data():
    data = {
        "Company": ["A", "B", "C"],
        "CurrentAssets": [100000, 150000, 120000],
        "CurrentLiabilities": [50000, 70000, 60000],
        "Inventory": [20000, 30000, 25000],
        "Cash": [30000, 40000, 35000],
        "TotalAssets": [300000, 400000, 350000],
        "TotalLiabilities": [180000, 250000, 220000],
        "Equity": [120000, 150000, 130000],
        "Sales": [500000, 650000, 600000],
        "COGS": [300000, 380000, 360000],
        "OperatingIncome": [120000, 160000, 140000],
        "NetIncome": [80000, 110000, 95000],
        "SharesOutstanding": [10000, 15000, 12000],
        "MarketPrice": [25, 30, 28],
    }
    return pd.DataFrame(data)


# ---------- Stage 2–4: Liquidity ----------
def current_ratio(df):
    df["Current_Ratio"] = df["CurrentAssets"] / df["CurrentLiabilities"]
    return df


def quick_ratio(df):
    df["Quick_Ratio"] = (df["CurrentAssets"] - df["Inventory"]) / df["CurrentLiabilities"]
    return df


def cash_ratio(df):
    df["Cash_Ratio"] = df["Cash"] / df["CurrentLiabilities"]
    return df


# ---------- Stage 5–6: Leverage ----------
def debt_to_equity_ratio(df):
    df["Debt_to_Equity"] = df["TotalLiabilities"] / df["Equity"]
    return df


def debt_ratio(df):
    df["Debt_Ratio"] = df["TotalLiabilities"] / df["TotalAssets"]
    return df


# ---------- Stage 7: Activity ----------
def inventory_turnover(df):
    df["Inventory_Turnover"] = df["COGS"] / df["Inventory"]
    return df


def total_asset_turnover(df):
    df["Total_Asset_Turnover"] = df["Sales"] / df["TotalAssets"]
    return df


# ---------- Stage 8: Profitability ----------
def gross_profit_margin(df):
    df["Gross_Profit_Margin"] = (df["Sales"] - df["COGS"]) / df["Sales"]
    return df


def net_profit_margin(df):
    df["Net_Profit_Margin"] = df["NetIncome"] / df["Sales"]
    return df


def roa(df):
    df["ROA"] = df["NetIncome"] / df["TotalAssets"]
    return df


def roe(df):
    df["ROE"] = df["NetIncome"] / df["Equity"]
    return df


# ---------- Stage 9: Market Ratios (FINAL) ----------
def eps(df):
    df["EPS"] = df["NetIncome"] / df["SharesOutstanding"]
    return df


def pe_ratio(df):
    df["P_E_Ratio"] = df["MarketPrice"] / df["EPS"]
    return df


def bvps(df):
    df["BVPS"] = df["Equity"] / df["SharesOutstanding"]
    return df


def pb_ratio(df):
    df["P_B_Ratio"] = df["MarketPrice"] / df["BVPS"]
    return df


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
    df = total_asset_turnover(df)

    # Profitability
    df = gross_profit_margin(df)
    df = net_profit_margin(df)
    df = roa(df)
    df = roe(df)

    # Market (FINAL)
    df = eps(df)
    df = pe_ratio(df)
    df = bvps(df)
    df = pb_ratio(df)

    print(df[[
        "Company",
        "EPS",
        "P_E_Ratio",
        "BVPS",
        "P_B_Ratio"
    ]])


if __name__ == "__main__":
    main()
