# Write your MySQL query statement below
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
)m
    ON e.departmentId = m.departmentId
   AND e.salary = m.max_salary; #getting max salary by department