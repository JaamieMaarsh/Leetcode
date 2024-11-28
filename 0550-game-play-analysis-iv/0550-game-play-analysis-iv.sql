  
# Write your MySQL query statement below
with min_date_CTE as (
    select player_id, min(event_date) as first_date
    from Activity 
    group by player_id
),
date_diff_CTE as (
    select a.player_id
    from Activity a join min_date_CTE b
    on a.player_id = b.player_id and 
    datediff(a.event_date, b.first_date) = 1
)

select 
round(count( distinct dd.player_id)/count( distinct md.player_id),2) as fraction
FROM min_date_CTE md
LEFT JOIN date_diff_CTE dd
ON md.player_id = dd.player_id;



