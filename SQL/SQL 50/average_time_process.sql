-- Have to compare rows of end and start, to compute time
-- So self join is needed, based on machine id and process, so that they are on the same row
-- Then use where clause for start and end check, only for those rows compute time (Better to put in where instead of ON)
-- Group by machine id, and avg the difference and round to 3 places
-- In postgres, round only takes numeric so, cast it using ::
-- Every column in select must be in group by or in Aggregate function

SELECT A1.machine_id, ROUND(AVG(A2.timestamp - A1.timestamp)::NUMERIC, 3) as processing_time
FROM Activity A1 JOIN Activity A2
ON A1.machine_id = A2.machine_id AND A1.process_id = A2.process_id
WHERE A1.activity_type = 'start' AND A2.activity_type = 'end'
GROUP BY A1.machine_id;