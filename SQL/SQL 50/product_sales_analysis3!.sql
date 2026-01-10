-- Since for each product id, lowest year is needed, first get that by grouping by product id, and min(year)
-- Now all columns of table for matching this row is needed, so use this result in subquery
-- We cannot straight away just mention all the columns without subquery
-- As in group by we have to mention columns in select, and the behaviour is ambigous if you list all columns,
-- For year you can get minimum, but for other columns which row is picked is not determined
-- Row selected for aggregate column will not be taken for other columns

select product_id, year as first_year, quantity, price
from Sales
where (product_id, year) IN (
    select product_id, min(year)
    from Sales
    group by product_id
);