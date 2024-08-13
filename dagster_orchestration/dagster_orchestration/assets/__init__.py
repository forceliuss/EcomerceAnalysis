import os
from dagster_dbt import DbtCliClientResource
from dagster_dbt import load_assets_from_dbt_project

resources = {
    "dbt": DbtCliClientResource(
        project_dir=os.getenv("DBT_PROJECT_DIR"),
        profiles_dir=os.getenv("DBT_PROFILES_DIR"),
    ),
}

dbt_assets = load_assets_from_dbt_project(
    project_dir=os.getenv("DBT_PROJECT_DIR"), profiles_dir=os.getenv("DBT_PROFILES_DIR"), key_prefix=["transformed_data"]
)