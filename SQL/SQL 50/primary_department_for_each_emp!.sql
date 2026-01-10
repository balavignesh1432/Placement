-- Subquery: Here using OR to handle condition where only one row for that employee id exists
-- And also returning rows where primary flag is true
select employee_id, department_id
from Employee
where primary_flag = 'Y' OR employee_id IN (
select employee_id 
from Employee 
group by employee_id 
having count(*) = 1);

-- UNION: Getting each condition and using UNION
-- Since postgres does not allow just grouping by employee id when also selecting department id (Need for union)
-- We can use aggregate say max(), this will not affect because when only one row of group max will be itself
-- Since here we only care about count of group should be 1
-- This is not needed for my sql
SELECT employee_id, department_id
FROM Employee
WHERE primary_flag = 'Y'

UNION

SELECT employee_id, MAX(department_id)
FROM Employee
GROUP BY employee_id
HAVING COUNT(*) = 1;