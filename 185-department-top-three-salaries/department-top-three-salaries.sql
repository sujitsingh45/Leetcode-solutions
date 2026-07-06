# Write your MySQL query statement b
select Department,Employee,Salary #selecting the output column from subquery
from(
select 
d.name  as Department,
e.name as Employee,
e.salary as Salary,
Dense_Rank() over(partition by d.name order by e.salary Desc) as rnk #Assign a rank to salaries within each department, Highest salary gets rank 1,Employees with the same salary receive the same rank
from Employee e 
left join Department d
on d.id=e.departmentId) p #End of subquery and name it 'p'
where p.rnk <=3;#taking only employees whose salary rank is 1, 2, or 3
