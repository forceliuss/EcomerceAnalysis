SELECT
    ORDER_ID,
    PAYMENT_TYPE,
    PAYMENT_VALUE
FROM
    {{ source("raw_data",
    "payments") }}