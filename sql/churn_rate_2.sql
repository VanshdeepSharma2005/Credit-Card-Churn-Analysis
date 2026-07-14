SELECT
    Card_Category,
    ROUND(COUNT(CASE WHEN Customer_Status = 'Attrited Customer' THEN 1 END) * 100.0 / COUNT(*),2) AS Churn_Rate 
    FROM customers
GROUP BY Card_Category
ORDER BY Card_Category;

-- CHURN RATE BASED ON CARD_CATEGORY