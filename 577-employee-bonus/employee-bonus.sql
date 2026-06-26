# Write your MySQL query statement below
select e.name,b.bonus #selecting require column
 from Employee e 
 left join Bonus b #right join on bonus table
 on e.empId=b.empId #joining by empid
 where b.bonus < 1000 # condition
  or b.bonus is null;
