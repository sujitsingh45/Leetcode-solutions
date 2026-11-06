# Write your MySQL query statement below
select actor_id, 
director_id

from ActorDirector e


group by 
actor_id,
director_id
having
count(*)>=3; 
#count(e.actor_id)>=3
#and count(e.director_id)>=3;
