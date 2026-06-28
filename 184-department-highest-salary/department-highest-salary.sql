/* # Write your MySQL query statement below
SELECT
    d.name AS Department, #selecting required column as per need 
    e.name AS Employee,
    e.salary AS Salary
FROM Employee e
JOIN Department d
    ON e.departmentId = d.id #solving by double join to avoid subquery 
JOIN (
    SELECT departmentId, MAX(salary) AS max_salary
    FROM Employee
    GROUP BY departmentId
)s
    ON e.departmentId = s.departmentId
   AND e.salary = s.max_salary; #getting max salary by department

    */
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