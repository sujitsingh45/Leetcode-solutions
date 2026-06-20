# Write your MySQL query statement below
select 
P.firstname,P.lastname,a.city,a.state #selecting the require column
 from Person p # person as p
left join   Address a # address as a and left join
on p.personid=a.personid #join on personid

