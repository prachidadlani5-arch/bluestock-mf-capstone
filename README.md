# 📊 Bluestock Mutual Fund Analytics

An end-to-end mutual fund analytics platform that ingests raw fund data, cleans and structures it into a relational database, computes industry-standard performance and risk metrics, and presents the results through an interactive **4-page Power BI dashboard** — extended with advanced risk, behavioural, and recommendation analytics.

Built as a capstone/internship project covering the full analytics lifecycle: **ETL → Cleaning → Database Design → EDA → Performance Analytics → Risk Analytics → Dashboarding → Advanced Analytics.**

---

## 🔎 Project Overview

Retail investors and analysts are often left comparing mutual funds using return figures alone, with fragmented data spread across NAV history, AUM reports, SIP inflows, and transaction logs, and little visibility into risk. **Bluestock Mutual Fund Analytics** solves this by unifying ten heterogeneous datasets into a single star-schema database, computing a full performance and risk scorecard for **40 mutual fund schemes**, and exposing the results through an interactive dashboard and a transparent rule-based recommender.

The project was built over six structured phases:

| Day | Focus |
|---|---|
| 1 | Data ingestion pipeline, live NAV fetching, environment setup |
| 2 | Data cleaning, validation, and SQLite star-schema database |
| 3 | Exploratory data analysis (NAV, AUM, SIP, category, investor trends) |
| 4 | Performance analytics — CAGR, Sharpe, Sortino, Alpha, Beta, Drawdown |
| 5 | 4-page interactive Power BI dashboard |
| 6 | Advanced analytics — VaR, CVaR, rolling Sharpe, cohorts, recommender, HHI |

---

## ✨ Features

- **Automated ETL pipeline** ingesting 10 raw CSV datasets with live NAV-fetching support
- **Data cleaning & validation**: missing-value handling, duplicate removal, ISO date standardisation, business-rule checks
- **Star-schema SQLite database** loaded via SQLAlchemy for fast, join-friendly analytical queries
- **Interactive EDA** using Plotly — NAV trends, AUM growth, SIP inflows, category and investor patterns
- **Full performance scorecard** for 40 schemes: Daily Returns, CAGR (1Y/3Y), Sharpe Ratio, Sortino Ratio, Alpha, Beta, Maximum Drawdown, and a consolidated fund ranking
- **Benchmark comparison** against market indices (e.g., NIFTY 50)
- **4-page Power BI dashboard**: Industry Overview, Fund Performance, Investor Analytics, SIP & Market Trends — with slicers, drill-through pages, and custom tooltips
- **Advanced analytics module**: Historical VaR (95%), CVaR, rolling 90-day Sharpe Ratio, investor cohort analysis, SIP continuity analysis, portfolio concentration (HHI)
- **Rule-based mutual fund recommender** (`recommender.py`) for transparent, explainable fund suggestions

---

## 📁 Folder Structure

```
bluestock-mutual-fund-analytics/
│
├── data/
│   ├── raw/
│   │   ├── 01_fund_master.csv
│   │   ├── 02_nav_history.csv
│   │   ├── 03_aum_by_fund_house.csv
│   │   ├── 04_monthly_sip_inflows.csv
│   │   ├── 05_category_inflows.csv
│   │   ├── 06_industry_folio_count.csv
│   │   ├── 07_scheme_performance.csv
│   │   ├── 08_investor_transactions.csv
│   │   ├── 09_portfolio_holdings.csv
│   │   └── 10_benchmark_indices.csv
│   └── processed/
│       └── mutual_fund.db              # cleaned SQLite star-schema database
│
├── notebooks/
│   ├── 01_data_ingestion.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_eda.ipynb
│   ├── 04_performance_analytics.ipynb
│   └── 05_advanced_analytics.ipynb
│
├── src/
│   ├── ingestion.py
│   ├── cleaning.py
│   ├── database.py
│   ├── performance_metrics.py
│   ├── risk_metrics.py
│   └── recommender.py
│
├── reports/
│   ├── var_cvar_report.csv
│   ├── sector_hhi.csv
│   ├── rolling_sharpe_chart.png
│   └── fund_scorecard.csv
│
├── dashboard/
│   └── Bluestock_Mutual_Fund_Dashboard.pbix
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

**Prerequisites:** Python 3.9+, Power BI Desktop (Windows, for viewing/editing the dashboard), Git

```bash
# Clone the repository
git clone https://github.com/[username]/bluestock-mutual-fund-analytics.git
cd bluestock-mutual-fund-analytics

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

**`requirements.txt`** includes: `pandas`, `numpy`, `matplotlib`, `plotly`, `sqlalchemy`, `jupyter`

---

## ▶️ How to Run

1. **Ingest & clean the data**
   ```bash
   python src/ingestion.py
   python src/cleaning.py
   ```
2. **Build the database**
   ```bash
   python src/database.py
   ```
   This creates `data/processed/mutual_fund.db`, the SQLite star-schema database used by both the analytics scripts and Power BI.
3. **Run performance & risk analytics**
   ```bash
   python src/performance_metrics.py
   python src/risk_metrics.py
   ```
   Outputs the Fund Scorecard, VaR/CVaR report, rolling Sharpe chart, and HHI concentration report to `reports/`.
4. **Generate fund recommendations**
   ```bash
   python src/recommender.py --risk moderate --horizon 5
   ```
5. **Explore interactively** — open any notebook in `notebooks/` with:
   ```bash
   jupyter notebook
   ```

---

## 📈 Dashboard

The Power BI dashboard (`dashboard/Bluestock_Mutual_Fund_Dashboard.pbix`) connects directly to `mutual_fund.db` and contains four pages:

| Page | Contents |
|---|---|
| **1. Industry Overview** | KPI cards (Total AUM, Monthly SIP, Total Folios, Total Schemes), Industry AUM trend, AUM by AMC |
| **2. Fund Performance** | Return-vs-Risk scatter plot, fund table, NAV vs. Benchmark, slicers by Fund House / Category / Plan |
| **3. Investor Analytics** | Transactions by state, SIP/Lumpsum/Redemption donut, age-group analysis, monthly transactions |
| **4. SIP & Market Trends** | Category heatmap, SIP vs. NIFTY 50, top categories, month filter |

Enhanced with **drill-through pages**, **custom tooltips**, and **cross-page interactive filters**.

To view: open the `.pbix` file in Power BI Desktop and click **Refresh** to reload from the local database.

---

## 🏆 Results

- **Highest Sharpe Ratio:** Mirae Asset Large Cap Fund
- **Highest Sortino Ratio:** Mirae Asset Large Cap Fund
- **Highest Value-at-Risk (95%):** SBI Small Cap Fund
- **Full ranking generated for all 40 mutual fund schemes**, combining CAGR, Sharpe, Sortino, and drawdown into a single Fund Scorecard

These results are consistent with expected risk-return patterns across market-cap categories: large-cap exposure showing stronger risk-adjusted returns, and small-cap exposure carrying materially higher tail risk.

---

## 🛠️ Technologies

`Python` · `Pandas` · `NumPy` · `Matplotlib` · `Plotly` · `SQLite` · `SQLAlchemy` · `Power BI` · `Git` · `GitHub` · `Jupyter Notebook` · `VS Code`

---

## 🚀 Future Work

- Migrate from SQLite to a cloud-hosted database (e.g., PostgreSQL) for scale and concurrent access
- Automate the live NAV-fetch routine as a scheduled job for near-real-time refresh
- Replace the rule-based recommender with a machine-learning-based recommendation model
- Add parametric and Monte Carlo VaR to cross-validate historical simulation results
- Publish the dashboard to the Power BI Service with row-level security for role-based access
- Add a natural-language query layer over the database for non-technical users

---

## 👤 Author

**[Student Name]**
B.Tech, Computer Science & Engineering (AI & Data Science)
📧 [student.email@example.com] · 🔗 [LinkedIn Profile] · 💻 [GitHub Profile]

---

*If you find this project useful, consider giving it a ⭐ on GitHub!*
