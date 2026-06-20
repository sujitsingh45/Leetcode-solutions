# Write your MySQL query statement below
select 
Person.firstname,Person.lastname,Address.city,Address.state #selecting the require column
 from Person  
left join Address 
on Person.personid=Address.personid #join on personid

