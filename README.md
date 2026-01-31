# financial-analysis
Financial data analysis, modeling, and experiments in Python

📊Financial Analysis & Distress Prediction Framework

📌 Project Overview
This project provides a comprehensive, modular, and extensible financial analysis framework designed for academic research and professional financial analysis.
The framework performs end-to-end processing of firm-level financial data, including:

- Financial ratio analysis

- Market and valuation ratios

- Cost of capital estimation

- Asset pricing models

- Financial distress prediction using machine learning

- Automated graphical and textual reporting

The system is designed so that users only need to provide an Excel input file, and the entire analytical pipeline is executed automatically.

🎯 Objectives
The primary objectives of this project are:

To compute and interpret core financial ratios across liquidity, profitability, leverage, and efficiency dimensions

To perform valuation and cost of capital analysis using CAPM, WACC, and DCF

To estimate risk factor sensitivities using the Fama–French three-factor model

To predict financial distress using statistical and machine learning models

To ensure data quality robustness and graceful handling of missing information

To generate professional numerical, graphical, and textual outputs suitable for academic and applied use

🧱 Project Structure
```financial-analysis/
│
├── data/
│   └── financial_data.xlsx        # User-provided input data
│
├── outputs/
│   ├── financial_analysis_results.xlsx
│   └── textual_report.txt
│
├── src/
│   ├── main.py                    # Main execution pipeline
│   ├── financial_ratios.py        # Accounting-based financial ratios
│   ├── market_ratios.py           # Market and valuation ratios
│   ├── data_quality.py            # Data validation and quality control
│   ├── textual_report.py          # Automated academic-style report
│   │
│   ├── data_loader.py             # (Reserved for future refactoring)
│   ├── valuation.py               # (Reserved for modular valuation logic)
│   ├── regression.py              # (Reserved for econometric models)
│   ├── utils.py                   # (Reserved for helper utilities)
│   └── __init__.py
│
└── README.md
Note: Some modules are intentionally left as placeholders to preserve a scalable and modular architecture for future development and refactoring.

🔬 Analytical Phases
The pipeline is organized into clearly defined analytical phases:

Phase 0 – Data Quality Control
Detection of missing or inconsistent values

Warning-based handling (no artificial data injection)

Ensures robustness for real-world datasets

Phase 1 – Financial Ratio Analysis
Includes:

Liquidity ratios (Current, Quick, Cash)

Profitability ratios (Margins, ROA, ROE)

Leverage ratios (Debt ratios, Interest coverage)

Efficiency ratios (Turnovers)

Each ratio is calculated only if required inputs are available, otherwise skipped with a warning.

Phase 2 – Valuation & Cost of Capital
CAPM expected return estimation

Weighted Average Cost of Capital (WACC)

Discounted Cash Flow (DCF) valuation

These models provide insight into firm value and capital structure efficiency.

Phase 3 – Asset Pricing & Financial Distress
Fama–French three-factor regression (Alpha, factor loadings)

Financial distress prediction using:

Logistic Regression

Neural Network (MLP)

This phase combines econometric rigor with machine learning methods.

Phase 6 – Market & Valuation Ratios
P/E, P/B, EV/EBITDA

Dividend yield

Market capitalization-based indicators

These metrics link accounting data to market perception.

📈 Outputs
The framework automatically generates:

1. Excel Output
financial_analysis_results.xlsx

- Summary sheet with all calculated variables

- Embedded charts for each numeric metric

2. Textual Report
textual_report.txt

- Formal, academic-style financial interpretation

- Suitable for reports, theses, or executive summaries

⚙️ How to Run
Place your input data in:

data/financial_data.xlsx
Ensure required Python packages are installed.

Run:

python src/main.py
All outputs will be created automatically.

🧠 Design Philosophy
Modular and extensible architecture

No hard-coded assumptions about data completeness

Academic transparency and reproducibility

Professional-grade reporting

The framework is suitable for:

Academic research

Financial analysis coursework

Risk management studies

Professional prototyping


🚀 Future Extensions
Planned or possible extensions include:

Panel data regression models

Time-series forecasting

Bankruptcy prediction models (Altman, Ohlson, Zmijewski)

Visualization dashboards

Full modular refactoring into reserved modules

👤 Author
Sara Rostami
Financial Engineering & Risk Management