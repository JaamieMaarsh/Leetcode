# Write your MySQL query statement below
# Write your MySQL query statement below
with first_order as (
    select customer_id, min(order_date) as first_order_date
    from Delivery
    group by customer_id
),
first_order_details as (
    select d.delivery_id, fo.customer_id, fo.first_order_date, d.customer_pref_delivery_date, 
    case when (first_order_date = customer_pref_delivery_date) 
    then "immediate" else "scheduled" end as type_of_delivery
    from  delivery d join first_order fo on d.customer_id = fo.customer_id 
    and d.order_date = fo.first_order_date
    -- group by customer_id
)

#select customer_id, type_of_delivery from first_order_details
SELECT ROUND(
           SUM(CASE WHEN type_of_delivery = 'immediate' THEN 1 ELSE 0 END) 
           / COUNT(customer_id) * 100, 
           2
       ) AS immediate_percentage
from first_order_details


