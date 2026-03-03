🏢 Vendor Performance & Profitability Analytics
📌 Project Overview

This project analyzes vendor sales, purchase, profitability, and inventory performance using Python (EDA + Statistical Analysis) and Power BI (Interactive Dashboarding).

The objective was to identify:

High & low performing vendors

Profitability drivers

Capital locked in unsold inventory

Pricing optimization opportunities

Contribution concentration (Pareto analysis)

📊 Key Metrics
KPI	Value
Total Sales	$441M
Total Purchase	$307M
Gross Profit	$134M
Profit Margin	38.7%
Unsold Capital	$2.7M
🔍 Analysis Performed
1️⃣ Exploratory Data Analysis (Python)

Distribution plots (Histograms + KDE)

Boxplots for outlier detection

Correlation heatmap

Vendor & brand frequency analysis

Summary statistics interpretation

2️⃣ Business Analysis
🔹 Pareto Analysis

Top 10 vendors contribute ~65% of total purchases.

🔹 Brand Optimization Insight

Identified brands with low sales but high margins — candidates for promotional strategies.

🔹 Inventory Risk Modeling

Calculated unsold inventory value:

UnsoldInventoryValue = (TotalPurchaseQuantity - TotalSalesQuantity) * PurchasePrice

Detected $2.7M+ capital locked in slow-moving inventory.

3️⃣ Statistical Inference

Segmented vendors using Q1/Q3 sales thresholds.

Computed 95% confidence intervals for profit margins.

Found low-performing vendors maintain significantly higher margins.

📈 Power BI Dashboard

Dashboard includes:

KPI Summary Cards

Purchase Contribution Donut Chart

Top Vendors by Sales

Top Brands by Sales

Low Performing Vendors (Stock Turnover)

Profit Margin vs Sales Scatter Analysis

📌 Power BI file (.pbix) will be uploaded soon.

🛠 Tools & Technologies

Python (Pandas, NumPy, Seaborn, Matplotlib)

Statistical Analysis (t-distribution CI)

SQL

Power BI

DAX
