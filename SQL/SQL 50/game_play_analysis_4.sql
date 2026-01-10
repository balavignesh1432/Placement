-- We need the first login for each player so get that using min(date) and group by player id
-- Then for each row in the table, whose player id in the subquer and login date is the next date
-- Count those distinct players, divide by total distinct players to get the fraction
select ROUND(count(DISTINCT player_id) / (Select count(DISTINCT player_id) from Activity)::numeric, 2) as fraction
from Activity
where (player_id, event_date) IN (Select player_id, min(event_date) + 1 from Activity group by player_id);