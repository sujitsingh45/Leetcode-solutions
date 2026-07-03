# Write your MySQL query statement below
select 
id,movie,description,rating # selecting required column 
from Cinema
where id%2!=0 and description != "boring" #condition not even and boring 
order by rating DESC; #table in dsecending order 