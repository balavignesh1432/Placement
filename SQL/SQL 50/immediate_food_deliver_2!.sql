-- First find the first order for each customer id by grouping and then min(date)
-- Then in the outer query only list rows that match the customer id and order date
-- For those rows find how many has matching order and prefer date using case when
-- Divide by row count to get the percentage
select ROUND(SUM(
    case 
        when order_date = customer_pref_delivery_date then 1
        else 0
    end
)/COUNT(*)::numeric * 100, 2) as immediate_percentage from Delivery
where (customer_id, order_date) IN (
select customer_id, min(order_date)
from Delivery
group by customer_id
);