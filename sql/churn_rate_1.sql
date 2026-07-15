SELECT cf.Card_Category,cf.Annual_Fee,cf.Reward_Rate,COUNT(*) AS Total_Customers,
COUNT(CASE WHEN c.Customer_Status = 'Attrited Customer' THEN 1 END) AS Churned_Customers,
ROUND(COUNT(CASE WHEN c.Customer_Status = 'Attrited Customer' THEN 1 END) * 100.0 / COUNT(*),2) AS Churn_Rate
FROM customers c
JOIN card_features cf
ON c.Card_Category = cf.Card_Category
GROUP BY cf.Card_Category, cf.Annual_Fee, cf.Reward_Rate;

-- SINCE MY REWARD RATE AND ANUUAL FEES DATA WERE PERFECTLY CORRELATED SO I INTERPRETED THEM TOGETHER

SELECT
    Income_Category,
    COUNT(*) AS Churned_Customers
FROM customers
WHERE Customer_Status = 'Attrited Customer'
GROUP BY Income_Category
ORDER BY Churned_Customers DESC;

-- CHURN RATE OF LESS THAN $40K IS HIGHER