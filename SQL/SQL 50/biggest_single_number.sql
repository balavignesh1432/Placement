-- Get the single number by group by having count 1
-- Then to get maximum, perform max on this subquery
select max(num) as num from 
(
    select num
    from myNumbers
    group by num
    having count(*) = 1
);