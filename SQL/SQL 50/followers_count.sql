-- Just count the number of user_id
-- So group by user_id, then sort it ascending
select user_id, count(*) as followers_count from Followers
group by user_id
order by user_id; 