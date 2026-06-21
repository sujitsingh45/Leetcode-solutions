# Write your MySQL query statement below
select max(salary)as SecondHighestSalary  # taking column name as second highest salary 
from Employee # from employee table
where salary < (select max(salary) from Employee); # extracting second highest salary using sub query