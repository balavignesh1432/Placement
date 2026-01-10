-- SUB QUERY: Manager id should should not exist in employee id column,
-- For those entries display employee_id
-- Also condition on salary
select employee_id 
from Employees
Where manager_id is not null and manager_id not in (
    select employee_id from Employees
) and salary < 30000
order by employee_id;

-- Optimal Join: Using self outer join, manager should exist in table 1 but for that entry there should not exist employee in table 2
-- Join based on e1 manager id and e2 employee id
-- But we will only deal with rows where there is manager but not employee
SELECT e1.employee_id
FROM Employees e1
FULL OUTER JOIN Employees e2
ON e1.manager_id = e2.employee_id
WHERE e1.salary < 30000 AND e2.employee_id IS NULL AND e1.manager_id IS NOT NULL
ORDER BY employee_id;