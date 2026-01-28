import warnings
import numpy as np


def data_quality_checks(df):
    """
    Phase 0: Data Quality Control
    - Does NOT stop execution
    - Does NOT create fake data
    - Flags invalid rows and warns user
    """

    df = df.copy()

    # -----------------------
    # Initialize flags
    # -----------------------
    df['DQ_Invalid_Assets'] = False
    df['DQ_Negative_Equity'] = False
    df['DQ_Invalid_WACC'] = False
    df['DQ_Invalid_FCF'] = False

    # -----------------------
    # Asset sanity check
    # -----------------------
    if 'TotalAssets' in df.columns:
        mask = df['TotalAssets'] <= 0
        if mask.any():
            warnings.warn(
                "Some observations have non-positive TotalAssets. Related ratios may be skipped.",
                RuntimeWarning
            )
            df.loc[mask, 'DQ_Invalid_Assets'] = True

    # -----------------------
    # Equity check
    # -----------------------
    if 'Equity' in df.columns:
        mask = df['Equity'] <= 0
        if mask.any():
            warnings.warn(
                "Negative or zero Equity detected. Leverage and market ratios may be unreliable.",
                RuntimeWarning
            )
            df.loc[mask, 'DQ_Negative_Equity'] = True

    # -----------------------
    # Free Cash Flow check
    # -----------------------
    if 'FCF' in df.columns:
        mask = df['FCF'].isna()
        if mask.any():
            warnings.warn(
                "Missing FCF values detected. DCF valuation will be skipped for these rows.",
                RuntimeWarning
            )
            df.loc[mask, 'DQ_Invalid_FCF'] = True

    # -----------------------
    # WACC logical range check
    # -----------------------
    if 'WACC' in df.columns:
        mask = (df['WACC'] <= 0) | (df['WACC'] > 1)
        if mask.any():
            warnings.warn(
                "Invalid WACC values detected (<=0 or >100%). DCF results may be invalid.",
                RuntimeWarning
            )
            df.loc[mask, 'DQ_Invalid_WACC'] = True

    return df
