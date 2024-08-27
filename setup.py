from setuptools import find_packages, setup

setup(
    name="modern-data-stack-project",
    packages=find_packages(),
    install_requires=[
        "dbt-bigquery",
        "dagster",
        "dagster-cloud",
        "dagster-dbt",
        "dagster-airbyte",
        "streamlit",
        "plotly-express"
        "pandas"
        "numpy"
        "google-cloud-bigquery"
    ],
    extras_require={"dev": ["dagit", "pytest"]},
)