-- Since for Every student and Subject, First perform cross join
-- then only that much row is required, so perfrom left join with Examinations and group by to keep that many rows
-- We need count of only matching, that is not null on right, so count() calculates only 
-- And every column in select must be in group by
SELECT Students.student_id, Students.student_name, Subjects.subject_name, COUNT(Examinations.student_id) as attended_exams
FROM Students CROSS JOIN Subjects
LEFT JOIN Examinations ON Examinations.student_id=Students.student_id AND Examinations.subject_name=Subjects.subject_name
GROUP BY Students.student_id, Students.student_name, Subjects.subject_name
ORDER BY Students.student_id, Subjects.subject_name;