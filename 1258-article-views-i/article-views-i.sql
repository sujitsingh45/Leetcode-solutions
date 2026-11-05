# Write your MySQL query statement below
select distinct #selecting distinct authoer id 
author_id as id
from views
where author_id=viewer_id  #matching author and viewer
order by id ASC;