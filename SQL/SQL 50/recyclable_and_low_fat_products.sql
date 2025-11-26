/* 
    Condition low fats and recyclable has to be 'Y'
    For those rows, only display product id
*/
SELECT product_id
FROM Products
WHERE low_fats = 'Y' AND recyclable = 'Y';