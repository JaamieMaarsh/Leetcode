# Write your MySQL query statement below
-- condition 1: when primary flag is 'Y' or
-- condition 2: count(distinct employee_id) = 1

# Write your MySQL query statement below
select employee_id, department_id
from Employee  
where primary_flag='Y' or employee_id in 
(select employee_id from Employee group by employee_id having count(*) = 1 )
