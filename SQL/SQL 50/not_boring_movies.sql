-- Rows have to be odd, so using id for row number as it is same
-- description should not be boring, 
-- So combine both using AND in WHERE clause
-- Use <> for inequality
-- For odd, use % 2 check
SELECT * 
FROM Cinema
WHERE id % 2 <> 0 AND description <> "boring"
ORDER BY rating DESC;