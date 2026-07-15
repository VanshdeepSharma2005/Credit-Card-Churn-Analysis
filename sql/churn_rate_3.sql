SELECT CASE
WHEN Age BETWEEN 20 AND 30 THEN '20-30'
WHEN Age BETWEEN 31 AND 40 THEN '31-40'
WHEN Age BETWEEN 41 AND 50 THEN '41-50'
WHEN Age BETWEEN 51 AND 60 THEN '51-60'
ELSE '60+'
END AS Age_Group,

COUNT(*) AS Total_Customers,

SUM(CASE
WHEN Customer_Status = 'Attrited Customer'
THEN 1 ELSE 0
END) AS Churned_Customers,

ROUND(SUM(CASE
WHEN Customer_Status = 'Attrited Customer'
THEN 1 ELSE 0 END) * 100.0 / COUNT(*),2) AS Churn_Rate

FROM customers
GROUP BY Age_Group
ORDER BY Churn_Rate DESC;