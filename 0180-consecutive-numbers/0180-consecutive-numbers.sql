# Write your MySQL query statement below
with consq_num as (
select num, 
lead(num) OVER (ORDER BY id) AS next_num,
lag(num) OVER (ORDER BY id) AS prev_num
from Logs
)

select distinct num as ConsecutiveNums 
from consq_num
where num = next_num and num = prev_num