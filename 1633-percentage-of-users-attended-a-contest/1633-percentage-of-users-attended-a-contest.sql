# Write your MySQL query statement below
select r.contest_id, 
round(count(distinct u.user_id)/ (select count(*) from users) * 100, 2) as percentage
from Register r join Users u
on r.user_id = u.user_id
group by contest_id
order by percentage desc, r.contest_id asc