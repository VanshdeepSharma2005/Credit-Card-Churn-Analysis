SELECT c.*,cf.Annual_Fee,cf.Reward_Rate
FROM customers c
JOIN card_features cf
ON c.Card_Category = cf.Card_Category;

-- CLEANED FINAL TABLE


