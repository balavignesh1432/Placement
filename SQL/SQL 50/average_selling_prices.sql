-- Since Even for entries in Prices where no units sold is needed use left join
-- Join based on id and the date should lie in the range, can use between
-- D
SELECT Prices.product_id, COALESCE(ROUND(SUM(price * units)/SUM(units)::NUMERIC, 2), 0) as average_price
FROM Prices LEFT JOIN UnitsSold
ON Prices.product_id = UnitsSold.product_id AND (purchase_date BETWEEN start_date AND end_Date OR purchase_date IS NULL)
GROUP BY Prices.product_id;