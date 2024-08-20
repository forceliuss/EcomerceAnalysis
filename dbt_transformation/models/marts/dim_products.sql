select 
    product_id,
    product_category_name,
    product_weight_g,
    sum(product_weight_g) as total_weight
from {{ ref("stg_products") }} group by product_category_name, product_id, product_weight_g