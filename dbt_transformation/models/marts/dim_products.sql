with
    products as (select * from {{ ref("stg_products") }}),
    item as (select * from {{ ref("stg_order_items") }}),
    products_stock as (
        select
            p.product_id,
            i.order_id,
            i.product_price,
            count(i.order_item_id) as products_sold
        from item i
        inner join products p using (product_id)
        group by p.product_id, i.order_id, i.product_price
    )
select *
from products_stock