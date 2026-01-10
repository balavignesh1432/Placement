-- Since table can contain duplicates
-- Count of unique products within the group, must be size of the products table
-- Even though not in the select, condition on the product_key can be performed in the having clause
select customer_id
from Customer
group by customer_id
having count(DISTINCT product_key) = (Select count(*) from Product)