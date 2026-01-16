🍔 Restaurant Sales Analytics (End-to-End Project)
By Pravar Kulshrestha
This project analyzes restaurant sales performance across products, cities, managers, purchase types, and dates — using a full data pipeline from raw CSV to dashboards.
________________________________________
🚀 Project Pipeline (End to End)
1️⃣ Python — Data Cleaning
Tasks performed:
•	Converted data types (date, numeric)
•	Removed duplicates & nulls
•	Standardized text fields (city, manager, product names)
•	Added Revenue = Price × Quantity
•	Exported clean dataset
Output:
Restaurant-Sales-CLEAN.csv
________________________________________
2️⃣ MySQL — Storage & Analysis
Loaded the clean CSV into MySQL and ran queries to analyze:
•	Total revenue & quantity sold
•	Revenue by product / city / manager
•	Online vs in-store vs drive-thru
•	Payment method usage
•	Time trends (daily, monthly, weekday)
All SQL queries included in:
sql/restaurant_analysis_queries.sql
________________________________________
3️⃣ Python — Automated SQL → Excel Pipeline
A script connects to MySQL, runs all analysis queries automatically, and outputs a single Excel file with multiple sheets.
pipeline/export_summary_to_excel.py
Generates:
output/Restaurant_Summary_<date>.xlsx
No manual exports required.
________________________________________
4️⃣ Power BI — Interactive Dashboard
Two-page report built from SQL data.
📌 Page 1 — Business Overview
•	Total revenue & units sold
•	Revenue by product
•	Revenue by purchase type (online / in-store / drive-thru)
•	Revenue by payment method
•	Revenue by city
•	Interactive slicers
📌 Page 2 — Manager & Time Insights
•	Top vs bottom manager performance
•	Revenue by manager
•	Product mix by manager
•	Revenue trends over time
•	Daily revenue volume
•	Filters for product / city / manager
Screenshots included in /powerbi/ folder.
________________________________________
📊 Key Findings
📌 Business Performance
•	Burgers generate nearly 50%+ of total revenue
•	Fries & Beverages sell consistently but lower ticket value
📌 City & Location
•	Lisbon & London outperform all cities
•	Paris & Berlin lag — possible sales/marketing opportunities
📌 Managers
•	Joao Silva & Tom Jackson drive majority of revenue
•	Lower-performing managers suggest coaching/training need
📌 Customer Behavior
•	Online purchases lead, followed by drive-thru
•	Credit card is dominant payment method
📌 Time Patterns
•	Sales trend upward across weeks
•	Weekends generate spikes
•	Isolated low-sales days suggest staffing or demand variability
________________________________________
🎯 Recommendations
•	Double down on best sellers (burgers)
•	Push weekday offers to flatten dips
•	Incentivize online orders (loyalty + delivery partnerships)
•	Study top manager practices & train lower performers
•	Promote underperforming cities through localized campaigns

