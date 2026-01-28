# src/textual_report.py

import numpy as np
from datetime import datetime


def _safe_value(val, digits=2):
    if val is None or (isinstance(val, float) and np.isnan(val)):
        return None
    return round(val, digits)


def generate_textual_report(df, output_path="../outputs/textual_report.txt"):
    """
    Phase 7: Professional & Academic Textual Financial Report
    Generates an interpretable financial analysis report for each firm.
    """

    lines = []
    lines.append("FINANCIAL ANALYSIS REPORT")
    lines.append("=" * 60)
    lines.append(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    lines.append("")

    for _, row in df.iterrows():
        company = row.get("Company", "Unknown Firm")

        lines.append("-" * 60)
        lines.append(f"Company: {company}")
        lines.append("-" * 60)

        # -------------------------
        # Liquidity
        # -------------------------
        cr = _safe_value(row.get("Current_Ratio"))
        qr = _safe_value(row.get("Quick_Ratio"))
        cashr = _safe_value(row.get("Cash_Ratio"))

        lines.append("Liquidity Position:")
        if cr is not None:
            lines.append(
                f"- The current ratio is {cr}, indicating the firm's ability to meet short-term obligations."
            )
        if qr is not None:
            lines.append(
                f"- The quick ratio of {qr} reflects liquidity excluding inventories."
            )
        if cashr is not None:
            lines.append(
                f"- The cash ratio stands at {cashr}, representing the most conservative liquidity measure."
            )

        # -------------------------
        # Profitability
        # -------------------------
        roa = _safe_value(row.get("ROA"))
        roe = _safe_value(row.get("ROE"))
        npm = _safe_value(row.get("Net_Profit_Margin"))

        lines.append("\nProfitability Analysis:")
        if roa is not None:
            lines.append(
                f"- Return on Assets (ROA) equals {roa}, indicating efficiency in using total assets to generate profits."
            )
        if roe is not None:
            lines.append(
                f"- Return on Equity (ROE) of {roe} reflects the return generated for shareholders."
            )
        if npm is not None:
            lines.append(
                f"- Net profit margin is {npm}, showing the proportion of revenue converted into net income."
            )

        # -------------------------
        # Leverage
        # -------------------------
        dte = _safe_value(row.get("Debt_to_Equity"))
        dta = _safe_value(row.get("Debt_to_Assets"))

        lines.append("\nCapital Structure and Financial Risk:")
        if dte is not None:
            lines.append(
                f"- Debt-to-equity ratio of {dte} suggests the degree of financial leverage employed by the firm."
            )
        if dta is not None:
            lines.append(
                f"- Debt-to-assets ratio equals {dta}, indicating the proportion of assets financed through liabilities."
            )

        # -------------------------
        # Efficiency
        # -------------------------
        at = _safe_value(row.get("Asset_Turnover"))
        it = _safe_value(row.get("Inventory_Turnover"))

        lines.append("\nOperational Efficiency:")
        if at is not None:
            lines.append(
                f"- Asset turnover of {at} reflects how effectively assets are utilized to generate revenue."
            )
        if it is not None:
            lines.append(
                f"- Inventory turnover of {it} indicates the efficiency of inventory management."
            )

        # -------------------------
        # Valuation
        # -------------------------
        wacc = _safe_value(row.get("WACC"))
        dcf = _safe_value(row.get("DCF_Value"))

        lines.append("\nValuation Indicators:")
        if wacc is not None:
            lines.append(
                f"- The weighted average cost of capital (WACC) is estimated at {wacc}, representing the firm's average financing cost."
            )
        if dcf is not None:
            lines.append(
                f"- The discounted cash flow (DCF) valuation yields an estimated firm value of {dcf}."
            )

        # -------------------------
        # Market Ratios
        # -------------------------
        pe = _safe_value(row.get("P_E_Ratio"))
        pb = _safe_value(row.get("P_B_Ratio"))
        dy = _safe_value(row.get("Dividend_Yield"))

        lines.append("\nMarket-Based Indicators:")
        if pe is not None:
            lines.append(
                f"- The price-to-earnings (P/E) ratio equals {pe}, reflecting market expectations of future earnings."
            )
        if pb is not None:
            lines.append(
                f"- The price-to-book (P/B) ratio of {pb} compares market value to accounting equity."
            )
        if dy is not None:
            lines.append(
                f"- Dividend yield stands at {dy}, representing cash return to shareholders."
            )

        # -------------------------
        # Financial Distress
        # -------------------------
        z = _safe_value(row.get("Z_Score"))
        logit = row.get("Distress_LogReg_Pred")
        nn = row.get("Distress_NN_Pred")

        lines.append("\nFinancial Distress Assessment:")
        if z is not None:
            lines.append(
                f"- The Altman Z-score is {z}, serving as an early warning indicator of financial distress."
            )
        if logit is not None:
            lines.append(
                f"- Logistic regression model predicts distress status as {int(logit)}."
            )
        if nn is not None:
            lines.append(
                f"- Neural network model predicts distress status as {int(nn)}."
            )

        lines.append("")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"Textual financial report saved to {output_path}")
