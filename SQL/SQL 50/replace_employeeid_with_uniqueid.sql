-- For all employees in Employee table, 
-- show name and unique_id if exists, other wise null
-- So left join based on common id column
SELECT unique_id, name
FROM Employees LEFT JOIN EmployeeUNI
ON Employees.id = EmployeeUNI.id;