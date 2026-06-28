# Write your MySQL query statement below
select 
d.name as Department,# selecting required column as per needed name
e.name as Employee,
e.salary as Salary
from Employee e
join Department d #inner join 
on e.departmentId =d.id #inner join on department id
where e.salary=(  #subquery
    select max(salary) as max_salary #getting max salary
    from Employee 
    where departmentid=e.departmentid #returning only one max rows
);