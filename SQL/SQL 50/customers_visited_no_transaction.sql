-- Get customers who visited but not transaction
-- Visit id is the common column, visitors data in visits table
-- And transaction data in Transactions table
-- Visit LEFT JOIN with transaction, and return values for which transaction is null
-- Use where clause with is null for it.
-- Need id wise count, so use group by along with count() and column alias

SELECT customer_id, count(customer_id) as count_no_trans
FROM Visits LEFT JOIN Transactions
ON Visits.visit_id = Transactions.visit_id
WHERE transaction_id IS NULL
GROUP BY customer_id;