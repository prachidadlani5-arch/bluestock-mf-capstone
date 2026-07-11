import pandas as pd

performance = pd.read_csv("data/processed/clean_scheme_performance.csv")

risk = input("Enter Risk Appetite (Low / Moderate / High): ")

recommended = (
    performance[
        performance["risk_grade"].str.lower() == risk.lower()
    ]
    .sort_values("sharpe_ratio", ascending=False)
    .head(3)
)

print("\nTop 3 Recommended Funds:\n")

print(
    recommended[
        [
            "scheme_name",
            "fund_house",
            "category",
            "sharpe_ratio",
            "risk_grade"
        ]
    ]
)