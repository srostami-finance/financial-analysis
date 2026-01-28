import pandas as pd
import numpy as np
import warnings


def _check_columns(df, required_cols, ratio_name):
    missing = [c for c in required_cols if c not in df.columns]
    if missing:
        warnings.warn(
            f"{ratio_name} not calculated. Missing columns: {missing}",
            RuntimeWarning
        )
        return False
    return True


def add_liquidity_ratios(df):
    if _check_columns(df, ['CurrentAssets', 'CurrentLiabilities'], 'Current Ratio'):
        df['Current_Ratio'] = df['CurrentAssets'] / df['CurrentLiabilities']

    if _check_columns(df, ['CurrentAssets', 'Inventory', 'CurrentLiabilities'], 'Quick Ratio'):
        df['Quick_Ratio'] = (df['CurrentAssets'] - df['Inventory']) / df['CurrentLiabilities']

    if _check_columns(df, ['Cash', 'CurrentLiabilities'], 'Cash Ratio'):
        df['Cash_Ratio'] = df['Cash'] / df['CurrentLiabilities']

    return df


def add_profitability_ratios(df):
    if _check_columns(df, ['Revenue', 'COGS'], 'Gross Margin'):
        df['Gross_Margin'] = (df['Revenue'] - df['COGS']) / df['Revenue']

    if _check_columns(df, ['OperatingIncome', 'Revenue'], 'Operating Margin'):
        df['Operating_Margin'] = df['OperatingIncome'] / df['Revenue']

    if _check_columns(df, ['NetIncome', 'Revenue'], 'Net Profit Margin'):
        df['Net_Profit_Margin'] = df['NetIncome'] / df['Revenue']

    if _check_columns(df, ['NetIncome', 'TotalAssets'], 'ROA'):
        df['ROA'] = df['NetIncome'] / df['TotalAssets']

    if _check_columns(df, ['NetIncome', 'Equity'], 'ROE'):
        df['ROE'] = df['NetIncome'] / df['Equity']

    return df


def add_leverage_ratios(df):
    if _check_columns(df, ['TotalLiabilities', 'TotalAssets'], 'Debt to Assets'):
        df['Debt_to_Assets'] = df['TotalLiabilities'] / df['TotalAssets']

    if _check_columns(df, ['TotalLiabilities', 'Equity'], 'Debt to Equity'):
        df['Debt_to_Equity'] = df['TotalLiabilities'] / df['Equity']

    if _check_columns(df, ['OperatingIncome', 'InterestExpense'], 'Interest Coverage'):
        df['Interest_Coverage'] = df['OperatingIncome'] / df['InterestExpense']

    return df


def add_efficiency_ratios(df):
    if _check_columns(df, ['Revenue', 'TotalAssets'], 'Asset Turnover'):
        df['Asset_Turnover'] = df['Revenue'] / df['TotalAssets']

    if _check_columns(df, ['COGS', 'Inventory'], 'Inventory Turnover'):
        df['Inventory_Turnover'] = df['COGS'] / df['Inventory']

    if _check_columns(df, ['Revenue', 'AccountsReceivable'], 'Receivables Turnover'):
        df['Receivables_Turnover'] = df['Revenue'] / df['AccountsReceivable']

    return df


def calculate_all_financial_ratios(df):
    """
    Master function for Phase 1
    """
    df = df.copy()

    df = add_liquidity_ratios(df)
    df = add_profitability_ratios(df)
    df = add_leverage_ratios(df)
    df = add_efficiency_ratios(df)

    return df
