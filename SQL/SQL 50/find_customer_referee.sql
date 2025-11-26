/*
Filter rows with referee is null or not equal to 2
Always use IS NULL to check equality with NULL
<> to check inequality
*/

SELECT name
FROM Customer
WHERE referee_id IS NULL OR referee_id <> 2;