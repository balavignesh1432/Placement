-- Use Left join to get row that do not have bonus also
SELECT name, bonus
FROM Employee LEFT JOIN Bonus
on Employeed.empID = Bonus.empID  AND Bonus.bonus < 1000;