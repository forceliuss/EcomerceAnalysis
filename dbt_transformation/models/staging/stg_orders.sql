SELECT
    ORDER_ID,
    CUSTOMER_ID,
    STATUS                        AS ORDER_STATUS,
    ORDER_APPROVED_AT,
    ORDER_DELIVERED_CUSTOMER_DATE,
    ORDER_ESTIMATED_DELIVERY_DATE
FROM
    {{ source("raw_data",
    "orders") }}