CREATE TABLE restaurant_sales (
    order_id INT,
    date DATE,
    product VARCHAR(50),
    price DECIMAL(10,2),
    quantity DECIMAL(10,2),
    purchase_type VARCHAR(20),
    payment_method VARCHAR(20),
    manager VARCHAR(50),
    city VARCHAR(50),
    revenue DECIMAL(12,2)
);
SELECT COUNT(*) FROM restaurant_sales;

SELECT * FROM restaurant_sales LIMIT 10;

SELECT MIN(date), MAX(date) FROM restaurant_sales;

SELECT SUM(revenue) AS total_revenue FROM restaurant_sales;

SELECT SUM(quantity) AS total_quantity FROM restaurant_sales;

SELECT product, SUM(revenue) AS revenue
FROM restaurant_sales
GROUP BY product
ORDER BY revenue DESC;

SELECT product, SUM(quantity) AS units
FROM restaurant_sales
GROUP BY product
ORDER BY units DESC;

SELECT city, SUM(revenue) AS revenue
FROM restaurant_sales
GROUP BY city
ORDER BY revenue DESC;

SELECT city, product, SUM(revenue) AS revenue
FROM restaurant_sales
GROUP BY city, product
ORDER BY city, revenue DESC;

SELECT manager, SUM(revenue) AS revenue
FROM restaurant_sales
GROUP BY manager
ORDER BY revenue DESC;

SELECT manager, product, SUM(revenue) AS revenue
FROM restaurant_sales
GROUP BY manager, product
ORDER BY manager, revenue DESC;

SELECT purchase_type, SUM(revenue) AS revenue
FROM restaurant_sales
GROUP BY purchase_type;

SELECT city, purchase_type, SUM(revenue) AS revenue
FROM restaurant_sales
GROUP BY city, purchase_type
ORDER BY city;

SELECT payment_method, SUM(revenue) AS revenue
FROM restaurant_sales
GROUP BY payment_method
ORDER BY revenue DESC;

SELECT city, payment_method, SUM(revenue) AS revenue
FROM restaurant_sales
GROUP BY city, payment_method
ORDER BY city;

SELECT date, SUM(revenue) AS revenue
FROM restaurant_sales
GROUP BY date
ORDER BY date;

SELECT DATE_FORMAT(date, '%Y-%m') AS month, SUM(revenue) AS revenue
FROM restaurant_sales
GROUP BY month
ORDER BY month;

SELECT DAYNAME(date) AS weekday, SUM(revenue) AS revenue
FROM restaurant_sales
GROUP BY weekday
ORDER BY revenue DESC;

SELECT city, manager, SUM(revenue) AS revenue
FROM restaurant_sales
GROUP BY city, manager
ORDER BY city, revenue DESC;

SELECT product, purchase_type, SUM(revenue) AS revenue
FROM restaurant_sales
GROUP BY product, purchase_type
ORDER BY product, revenue DESC;

SELECT payment_method, purchase_type, SUM(revenue) AS revenue
FROM restaurant_sales
GROUP BY payment_method, purchase_type
ORDER BY revenue DESC;
