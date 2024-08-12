select
    product_id,
    name as product_name,
    collection,
    category,
    price,
    availability,
    rating,
from {{ source("raw_data", "products") }}