-- Since for each date needed, group by date
-- count of distinct users needed 
-- specify the date range in where clause, simply subtract from given date string
-- since that day is also included diff should be between 0 and 29 not 30
SELECT activity_date as day, COUNT(DISTINCT user_id) as active_users
FROM Activity
WHERE '2019-07-27' - activity_date BETWEEN 0 AND 29
GROUP BY activity_date;