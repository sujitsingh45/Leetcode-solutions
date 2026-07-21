# Write your MySQL query statement below
select p.project_id,
ROUND(avg(e.experience_years),2) as average_years #avg with round 2 digits
from Project p
 join Employee e  #inner join on employee id
on p.employee_id=e.employee_id
group by p.project_id;  # grouping to get avverage 

