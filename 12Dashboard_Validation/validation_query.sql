-- SQL dashboard validation
SELECT
    SUM(Quantity * UnitPrice) AS TotalRevenue,
    COUNT(DISTINCT InvoiceNo) AS TotalOrders,
    SUM(Quantity) AS UnitsSold,
    COUNT(DISTINCT CustomerID) AS UniqueCustomers
FROM Sales;
