with
    orders as (select * from {{ ref("stg_orders")}}),
    payments as (select * from {{ ref("stg_payments")}}),
    payments_orders as (
        select
            o.order_id,
            o.customer_id,
            o.order_approved_at,
            o.order_status,
            p.payment_type,
            p.payment_value
        from orders o
        inner join payments p using (order_id)
        group by o.order_id, o.customer_id, o.order_approved_at, p.payment_value, o.order_status, 
            p.payment_type
    )
select *
from payments_orders