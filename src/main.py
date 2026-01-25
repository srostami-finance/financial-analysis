import numpy as np

def capm_expected_return(stock_returns, market_returns, risk_free_rate):
    """
    محاسبه Beta و بازده مورد انتظار سهم بر اساس مدل CAPM
    """
    beta = np.cov(stock_returns, market_returns)[0, 1] / np.var(market_returns)
    expected_return = risk_free_rate + beta * (market_returns.mean() - risk_free_rate)
    return beta, expected_return

def main():
    # داده نمونه: بازده سهم و بازار
    stock_returns = np.array([0.02, 0.03, -0.01, 0.04, 0.01])
    market_returns = np.array([0.015, 0.025, -0.005, 0.03, 0.01])
    risk_free_rate = 0.01

    # محاسبه Beta و بازده مورد انتظار
    beta, expected_return = capm_expected_return(
        stock_returns,
        market_returns,
        risk_free_rate
    )

    # نمایش نتایج
    print("CAPM Results:")
    print("Beta:", round(beta, 3))
    print("Expected Return:", round(expected_return, 3))

if __name__ == "__main__":
    main()
