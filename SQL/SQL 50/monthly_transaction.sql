-- Convert date to formatted string using TO_CHAR, specify the format
-- to count based on condition, use sum with case and 1 if true else 0
-- Dont use select alias in group by, repeat it

SELECT TO_CHAR(trans_date, 'YYYY-MM') as month,
country,
COUNT(id) AS trans_count,
SUM(
    CASE 
        WHEN state = 'approved' THEN 1
        ELSE 0
    END
) AS approved_count,
SUM(amount) AS trans_total_amount ,
SUM(
    CASE
        WHEN state = 'approved' THEN amount
        ELSE 0
    END
) AS approved_total_amount 
FROM Transactions
GROUP BY TO_CHAR(trans_date, 'YYYY-MM'), country;