-- We need records of employee id who has been manager, ie someone reports to them in reports to
-- So join based on that condition
-- E should be manager, F should be employee, so find average F.age, and just use ROUND() for nearest integer
-- Group by E.employee id, and perform aggregate count() and avg()
select E.employee_id, E.name, count(*) AS reports_count, ROUND(avg(F.age)) AS average_age 
from Employees E JOIN Employees F
on E.employee_id = F.reports_to
Group by E.employee_id, E.name
order by E.employee_id;