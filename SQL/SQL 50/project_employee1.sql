-- Average years of experience
-- Join using common column
-- Group by project, Perform avg and then round 2 decimal places
SELECT project_id, ROUND(AVG(experience_years), 2) as average_years
FROM Project INNER JOIN Employee
ON Project.employee_id = Employee.employee_id
GROUP BY project_id;