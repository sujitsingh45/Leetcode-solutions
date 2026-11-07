# Write your MySQL query statement below
select x,y,z,
case
when    x+y>z
   and  y+z>x
   and  z+x>y
   then 'Yes'
   else 'No'
end as triangle
from Triangle;
#sum of two side should be greater than the third in all condition   


   