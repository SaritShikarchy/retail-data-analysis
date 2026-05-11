-- revenue by country
SELECT Country, SUM(Revenue) AS total_revenue
FROM RETAIL_DB.PUBLIC.SALES
GROUP BY Country
ORDER BY total_revenue DESC;

-- revenue by month
SELECT Year, Month, SUM(Revenue) AS total_revenue
FROM RETAIL_DB.PUBLIC.SALES
GROUP BY Year, Month
ORDER BY Year, Month;

-- top products
SELECT Description, SUM(Quantity) AS total_quantity
FROM RETAIL_DB.PUBLIC.SALES
GROUP BY Description
ORDER BY total_quantity DESC
LIMIT 10;
