import pandas as pd
import mysql.connector as sql
from datetime import datetime

# ---------------------------
# 1️⃣ Connect to MySQL
# ---------------------------
conn = sql.connect(
    host='localhost',
    user='root',
    password='root',
    database='analysis'
)

# ---------------------------
# 2️⃣ Define ALL Analysis Queries
# ---------------------------
queries = {
    "total_revenue": """
        SELECT SUM(revenue) AS total_revenue
        FROM restaurant_sales
    """,

    "total_quantity": """
        SELECT SUM(quantity) AS total_quantity
        FROM restaurant_sales
    """,

    "product_revenue": """
        SELECT product, SUM(revenue) AS revenue
        FROM restaurant_sales
        GROUP BY product
        ORDER BY revenue DESC
    """,

    "product_units": """
        SELECT product, SUM(quantity) AS units
        FROM restaurant_sales
        GROUP BY product
        ORDER BY units DESC
    """,

    "city_revenue": """
        SELECT city, SUM(revenue) AS revenue
        FROM restaurant_sales
        GROUP BY city
        ORDER BY revenue DESC
    """,

    "city_product_revenue": """
        SELECT city, product, SUM(revenue) AS revenue
        FROM restaurant_sales
        GROUP BY city, product
        ORDER BY city, revenue DESC
    """,

    "manager_revenue": """
        SELECT manager, SUM(revenue) AS revenue
        FROM restaurant_sales
        GROUP BY manager
        ORDER BY revenue DESC
    """,

    "manager_product": """
        SELECT manager, product, SUM(revenue) AS revenue
        FROM restaurant_sales
        GROUP BY manager, product
        ORDER BY manager, revenue DESC
    """,

    "purchase_type_revenue": """
        SELECT purchase_type, SUM(revenue) AS revenue
        FROM restaurant_sales
        GROUP BY purchase_type
    """,

    "payment_method_revenue": """
        SELECT payment_method, SUM(revenue) AS revenue
        FROM restaurant_sales
        GROUP BY payment_method
        ORDER BY revenue DESC
    """,

    "daily_revenue": """
        SELECT date, SUM(revenue) AS revenue
        FROM restaurant_sales
        GROUP BY date
        ORDER BY date
    """,

    "monthly_revenue": """
        SELECT DATE_FORMAT(date, '%Y-%m') AS month, SUM(revenue) AS revenue
        FROM restaurant_sales
        GROUP BY month
        ORDER BY month
    """,

    "weekday_revenue": """
        SELECT DAYNAME(date) AS weekday, SUM(revenue) AS revenue
        FROM restaurant_sales
        GROUP BY weekday
        ORDER BY revenue DESC
    """
}

# ---------------------------
# 3️⃣ Create Output File Name
# ---------------------------
filename = f"Restaurant_Summary_{datetime.now().strftime('%Y%m%d')}.xlsx"

# ---------------------------
# 4️⃣ Execute Queries & Write to Excel
# ---------------------------
with pd.ExcelWriter(filename) as writer:
    for name, query in queries.items():
        df = pd.read_sql(query, conn)
        df.to_excel(writer, sheet_name=name[:31], index=False)  # sheet name max 31 chars
        print(f"Written: {name}")

conn.close()

print(f"\n🎉 DONE! File created → {filename}")
