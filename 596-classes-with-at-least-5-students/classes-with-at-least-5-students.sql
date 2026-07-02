# Write your MySQL query statement below
select 
class # required column
from Courses
group by class
Having  count(student) >4; #condition atleast 5 >=5