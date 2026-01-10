-- Percentage of users attended contest
-- subquery to count the rows in users, it only runs once, it is in select clause
-- Perform numeric casting for round
-- Group by contest enables to use count of users for each contest
select contest_id, ROUND((count(user_id)::numeric/(select count(user_id) from Users)) * 100, 2) as percentage
FROM Register
GROUP BY contest_id
ORDER BY percentage DESC, contest_id ASC;   