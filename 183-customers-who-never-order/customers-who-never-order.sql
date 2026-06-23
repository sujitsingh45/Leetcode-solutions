# Write your MySQL query statement below
select Customers.name as Customers #taking column name as Customers 
from Customers 
left join Orders #left join with orders table  
on Customers.id=Orders.customerId
where Orders.customerId is null; #extracting the one who orders
 

