-- Temperature greater than previous dates
-- Since comparison of rows in same table needs self join
-- Join such that date is one more than other date, POSTGRES just use + operator for next day
-- Now perform comparison between the two columns of same row using WHERE clause
SELECT w1.id
FROM Weather w1 JOIN Weather w2
ON w1.recordDate = w2.recordDate + 1
WHERE w1.temperature > w2.temperature;