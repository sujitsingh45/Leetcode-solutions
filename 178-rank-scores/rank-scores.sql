# Write your MySQL query below
select score, # required column
dense_rank() over (order by score desc) as 'rank' #taking one column as rank as it require and using dense_rank as per the condition 
from Scores;

