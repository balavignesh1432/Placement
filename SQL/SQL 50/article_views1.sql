-- Author has to view his article
-- Means viewer id has to be author id for the entry
-- Sort the ids in ascending ORDER
-- But no primary key, so there can be duplicate ids,
-- Use DISTINCT keyword to only list distinct ids
-- Use column alias for author_id as id

SELECT DISTINCT author_id as id
FROM Views
WHERE author_id = viewer_id
ORDER BY author_id ASC;