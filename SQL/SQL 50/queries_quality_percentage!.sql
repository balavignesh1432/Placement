-- Use CASE to count baseed on condition, 1 for true, 0 for false
-- Count(*) when used with group by only counts number of rows in the group
-- Instead sum()/count(*), avg() could be also used
SELECT query_name, 
ROUND(SUM(rating/position::numeric)/COUNT(*), 2) AS quality, 
ROUND((SUM(
    CASE 
        WHEN rating < 3 THEN 1 
        ELSE 0 
    END
    )/COUNT(*)::numeric) * 100, 2) AS poor_query_percentage
FROM Queries
GROUP BY query_name;