# Write your MySQL query statement below
select player_id,
min(event_date) as first_login#return the earliest date and changing to first_login
from Activity 
group by player_id;#group by player_id