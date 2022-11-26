# Write your MySQL query statement below

Select 
    id, 
    case when p_id is Null then 'Root'
         when id in (select distinct p_id from Tree) then 'Inner'
         else 'Leaf'
    end as type
from 
    Tree