
## Revenue by Country Analysis

Query:
SELECT Country, SUM(Revenue) AS total_revenue
FROM RETAIL_DB.PUBLIC.SALES
GROUP BY Country
ORDER BY total_revenue DESC;

Insight:
Revenue is highly concentrated in the United Kingdom, generating approximately 7.3M while all other countries generate less than 300K.

Business Interpretation:
This indicates a strong dependency on a single market and highlights a potential risk, as well as an opportunity to expand in other regions.

---

## Revenue by Month Analysis

Query:
SELECT Year, Month, SUM(Revenue) AS total_revenue
FROM RETAIL_DB.PUBLIC.SALES
GROUP BY Year, Month
ORDER BY Year, Month;

Insight:
Revenue shows fluctuations over time, with certain months generating higher sales compared to others, indicating seasonality in customer purchasing behavior.

Business Interpretation:
Sales are not evenly distributed throughout the year, suggesting that demand is influenced by seasonal trends. This can support better planning of inventory, marketing campaigns and promotions.

---

## Top Products Analysis

Query:
SELECT Description, SUM(Quantity) AS total_quantity
FROM RETAIL_DB.PUBLIC.SALES
GROUP BY Description
ORDER BY total_quantity DESC
LIMIT 10;

Insight:
AA few products generate most of the sales volume, with the top product exceeding 80K units sold.

Business Interpretation:
Customer demand is concentrated around a few high performing items, mainly low-cost decorative products, indicating an opportunity to expand similar product categories.

---

## Summary

Revenue is heavily concentrated in the UK market, while other European countries show growth potential.  
Sales are driven by a small number of high performing products alongside a broader range of lower volume items.  
In addition, revenue patterns over time suggest the presence of seasonal trends.

---

## Recommendations

Reduce dependency on the UK market by expanding efforts in other European countries.  
Focus on scaling high performing products and ensuring availability.  
Leverage seasonal trends by aligning marketing and inventory planning with peak periods.  
Expand product offerings in successful categories such as home decoration and gift items.
