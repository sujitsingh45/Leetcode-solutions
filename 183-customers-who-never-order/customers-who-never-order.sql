# Write your MySQL query statement below
select A.name as Customers
from Customers A#from customers table
left join Orders B #left join with orders table  
on A.id=B.customerId
where B.customerId is null; #extracting the one who orders
 

