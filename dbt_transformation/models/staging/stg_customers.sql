SELECT
    CUSTOMER_ID,
    CITY,
    STATE,
    ZIP_CODE_PREFIX
FROM
    {{ source("raw_data",
    "customers") }}