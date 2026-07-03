# Data Dictionary

## dim_fund

| Column | Type | Description |
|--------|------|-------------|
| amfi_code | INTEGER | Unique AMFI scheme code |
| scheme_name | TEXT | Mutual fund name |
| fund_house | TEXT | AMC Name |
| category | TEXT | Fund category |
| plan | TEXT | Direct/Regular |
| risk_grade | TEXT | Risk level |

---

## fact_nav

| Column | Type | Description |
|--------|------|-------------|
| amfi_code | INTEGER | Scheme code |
| date | DATE | NAV Date |
| nav | REAL | Net Asset Value |

---

## fact_transactions

| Column | Type | Description |
|--------|------|-------------|
| investor_id | INTEGER | Investor ID |
| transaction_date | DATE | Date |
| transaction_type | TEXT | SIP/Lumpsum/Redemption |
| amount_inr | REAL | Investment Amount |
| state | TEXT | Investor State |
| city | TEXT | Investor City |
| payment_mode | TEXT | Payment Method |
| kyc_status | TEXT | Verified/Pending |

---

## fact_performance

| Column | Type | Description |
|--------|------|-------------|
| return_1yr_pct | REAL | 1 Year Return |
| return_3yr_pct | REAL | 3 Year Return |
| return_5yr_pct | REAL | 5 Year Return |
| alpha | REAL | Alpha |
| beta | REAL | Beta |
| sharpe_ratio | REAL | Sharpe Ratio |
| expense_ratio_pct | REAL | Expense Ratio |

Source: Bluestock Internship Dataset