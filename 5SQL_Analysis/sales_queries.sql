-- Business SQL queries
SELECT SUM(Revenue) AS total_revenue
FROM sales;
SELECT COUNT(DISTINCT OrderID) AS total_orders
FROM sales;
SELECT
    strftime('%Y-%m', OrderDate) AS sales_month,
    SUM(Revenue) AS monthly_revenue,
    COUNT(DISTINCT OrderID) AS order_count
FROM sales
GROUP BY strftime('%Y-%m', OrderDate)
ORDER BY sales_month;
SELECT
    Category,
    SUM(Revenue) AS category_revenue,
    COUNT(DISTINCT OrderID) AS order_count
FROM sales
GROUP BY Category
ORDER BY category_revenue DESC;
SELECT
    Product,
    SUM(Revenue) AS product_revenue,
    RANK() OVER (ORDER BY SUM(Revenue) DESC) AS revenue_rank
FROM sales
GROUP BY Product
ORDER BY revenue_rank;
