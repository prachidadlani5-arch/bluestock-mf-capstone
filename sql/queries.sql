-- 1. Top 5 Funds by AUM

SELECT
scheme_name,
aum_crore

FROM fact_performance

ORDER BY aum_crore DESC

LIMIT 5;
-- 2. Average NAV

SELECT

AVG(nav) AS average_nav

FROM fact_nav;
-- 3. Average NAV Per Month

SELECT

strftime('%Y-%m',date) AS month,

AVG(nav) AS average_nav

FROM fact_nav

GROUP BY month

ORDER BY month;

-- 4. Number of Funds by Category

SELECT

category,

COUNT(*) AS total_funds

FROM dim_fund

GROUP BY category;
-- 5. Funds with Expense Ratio below 1%

SELECT

scheme_name,

expense_ratio_pct

FROM fact_performance

WHERE expense_ratio_pct<1;
-- 6. Average 3 Year Return

SELECT

AVG(return_3yr_pct)

FROM fact_performance;
-- 7. Transactions by State

SELECT

state,

COUNT(*) AS total_transactions

FROM fact_transactions

GROUP BY state

ORDER BY total_transactions DESC;
-- 8. Payment Mode Usage

SELECT

payment_mode,

COUNT(*)

FROM fact_transactions

GROUP BY payment_mode;
-- 9. KYC Status

SELECT

kyc_status,

COUNT(*)

FROM fact_transactions

GROUP BY kyc_status;
-- 10. Average AUM

SELECT

AVG(aum_crore)

FROM fact_aum;
