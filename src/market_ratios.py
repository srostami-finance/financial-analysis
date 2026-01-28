# src/market_ratios.py

import warnings

def _check_columns(df, required_cols, ratio_name):
    missing = [c for c in required_cols if c not in df.columns]
    if missing:
        warnings.warn(f"{ratio_name} not calculated. Missing columns: {missing}", RuntimeWarning)
        return False
    return True

def add_market_ratios(df):
    """
    Phase 6: Market/Valuation Ratios
    """
    df = df.copy()

    # P/E
    if _check_columns(df, ['MarketPrice', 'EPS'], 'P/E'):
        df['P_E'] = df['MarketPrice'] / df['EPS']

    # P/B
    if _check_columns(df, ['MarketPrice', 'BookValuePerShare'], 'P/B'):
        df['P_B'] = df['MarketPrice'] / df['BookValuePerShare']

    # EV/EBITDA
    if _check_columns(df, ['MarketCap', 'TotalLiabilities', 'Cash', 'EBITDA'], 'EV/EBITDA'):
        df['Enterprise_Value'] = df['MarketCap'] + df['TotalLiabilities'] - df.get('Cash', 0)
        df['EV_EBITDA'] = df['Enterprise_Value'] / df['EBITDA']

    # Dividend Yield
    if _check_columns(df, ['DividendPerShare', 'MarketPrice'], 'Dividend Yield'):
        df['Dividend_Yield'] = df['DividendPerShare'] / df['MarketPrice']

    return df
