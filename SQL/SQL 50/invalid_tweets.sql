-- If content length greater than 15, then deemed invalid
-- So use LENGTH() operator to get the length
-- Select only the tweet id column

SELECT tweet_id
FROM Tweets
WHERE LENGTH(content) > 15