SELECT
    PRODUCT_ID,
    PRODUCT_CATEGORY_NAME,
    PRODUCT_WEIGHT_G
FROM
    {{ source("raw_data",
    "products") }}