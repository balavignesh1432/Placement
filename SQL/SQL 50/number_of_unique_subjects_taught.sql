-- Since finally only unique teacher id should be there
-- Only group by teacher id
-- And count subject id for second column
-- But it could contain duplicates
-- So only count distinct ids
SELECT teacher_id, count(DISTINCT subject_id) as cnt
FROM Teacher
GROUP BY teacher_id;