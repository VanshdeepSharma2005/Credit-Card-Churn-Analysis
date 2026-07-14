create database credit_card_churn ;
use credit_card_churn ;

select * from customers
limit 5;

CREATE TABLE card_features (
    Card_Category VARCHAR(20) PRIMARY KEY,
    Annual_Fee INT,
    Reward_Rate DECIMAL(3,1)
);
INSERT INTO card_features
(Card_Category, Annual_Fee, Reward_Rate)
VALUES
('Blue', 500, 1.0),
('Silver', 1500, 1.5),
('Gold', 3000, 2.0),
('Platinum', 5000, 3.0);

SELECT * FROM card_features;

SELECT c.*,cf.Annual_Fee,cf.Reward_Rate
FROM customers c
JOIN card_features cf
ON c.Card_Category = cf.Card_Category;

select Round(count(case when Customer_Status='Attrited Customer' then 1 end)*100 /count(*) ,2) as Churn_Rate
from customers
