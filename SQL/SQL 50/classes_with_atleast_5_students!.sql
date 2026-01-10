-- count for each class, so group by class
-- But there is condition to result only count greater that 5, so use having
-- Can not use where here because aggregates cannot be used inside where, where is applied before grouping
select class
from Courses
group by class
having count(student) >= 5;

-- Optimized Prefer Join over IN for better performance
-- Self join based on id and manager id match
-- group by id, and specify condition inside having
select e.name from Employee e JOIN Employee f on e.id = f.managerId
group by e.id, e.name
having count(*) >= 5;