import pandas as pd
from sqlalchemy import create_engine
engine = create_engine("sqlite:///data/db/bluestock_mf.db")
nav = pd.read_csv("data/processed/clean_nav_history.csv")
transactions = pd.read_csv("data/processed/clean_investor_transactions.csv")
performance = pd.read_csv("data/processed/clean_scheme_performance.csv")
dim_fund = performance[
    [
        "amfi_code",
        "scheme_name",
        "fund_house",
        "category",
        "plan",
        "risk_grade"
    ]
].drop_duplicates()
dim_fund.to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False
)
nav.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)
transactions.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)
performance.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)
fact_aum = performance[
    [
        "amfi_code",
        "aum_crore"
    ]
]
fact_aum.to_sql(
    "fact_aum",
    engine,
    if_exists="replace",
    index=False
)
print("NAV rows:", len(nav))
print("Transaction rows:", len(transactions))
print("Performance rows:", len(performance))
print("Fund rows:", len(dim_fund))
print("AUM rows:", len(fact_aum))