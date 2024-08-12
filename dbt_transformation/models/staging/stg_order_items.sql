select
    order_id,
    order_item_id,
    product_price,
    product_id
from {{ source("raw_data", "order_items") }}