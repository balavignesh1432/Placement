-- For each sale in sales table, need product name from Product Table
-- So sales left join product using common product id column
SELECT product_name, year, price
FROM Sales LEFT JOIN Product
ON Sales.product_id=Product.product_id;