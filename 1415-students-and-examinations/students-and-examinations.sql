# Write your MySQL query statement below
select 
s.student_id,
s.student_name,
sub.subject_name,
count(e.subject_name) as Attended_exams
from Students s
cross join subjects sub  #to combine every subject with every student
left join Examinations e
on s.student_id=e.student_id
and sub.subject_name=e.subject_name
group by #grouping based on id name and subject name to get the the count of particular subject
s.student_id,
s.student_name,
sub.subject_name
order by  #result order on based on student id and subject name
s.student_id,
sub.subject_name;

