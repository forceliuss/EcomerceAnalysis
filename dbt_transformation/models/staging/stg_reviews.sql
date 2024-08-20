SELECT
    ORDER_ID,
    REVIEW_ID,
    REVIEW_SCORE
FROM
    {{ source("raw_data",
    "reviews") }}