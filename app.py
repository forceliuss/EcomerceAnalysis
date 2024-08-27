import streamlit as st
from google.oauth2 import service_account
from google.cloud import bigquery
import pandas as pd
import numpy as np
import plotly.express as px

# Create API client.
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"]
)
client = bigquery.Client(credentials=credentials)

# Perform query.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def run_query(query):
    query_job = client.query(query)
    rows_raw = query_job.result()
    # Convert to list of dicts. Required for st.cache_data to hash the return value.
    rows = [dict(row) for row in rows_raw]
    return rows

def home():
    #Sidebar
    st.sidebar.title('Home')

def dashboard():
    #Importing Files
    """ df_payments = pd.read_csv("./data/raw/order_payments_dataset.csv", sep=",", usecols=['order_id','payment_value'])
    df_orders = pd.read_csv("./data/raw/orders_dataset.csv", sep=",", usecols=['order_id','order_approved_at'])

    df_merged = df_orders.merge(df_payments, how="inner", on='order_id')
    df_merged['order_approved_at'] = pd.to_datetime(df_merged['order_approved_at']).dt.floor('D')
    df_merged['order_approved_at'] = df_merged['order_approved_at'] """
    df_merged = pd.DataFrame(run_query("SELECT order_approved_at, payment_value FROM `olit-ecommerce.transformed_data.dim_orders`;"))\
        .sort_values(by='order_approved_at')
    df_merged['reveneu'] = df_merged['payment_value'].cumsum()

    st.title("Sales Overview")

    #Layout
    sec1 = st.container()

    with sec1:
        col1, col2, col3 = st.columns([1,1,1])

        with col1:
            st.metric(label="Temp", value="273 K", delta="1.2 K")

        with col2:
            st.metric(label="Temp", value="273 K", delta="1.2 K")

        with col3:
            st.metric(label="Temp", value="273 K", delta="1.2 K")

    sec2 = st.container()

    with sec2:
        sec2.subheader("Average Earnings")
        fig = px.line(df_merged, x="order_approved_at", y="reveneu")
        st.plotly_chart(fig, key="iris")

    sec3 = st.container()
    
    with sec3:
        df = run_query("SELECT * FROM `olit-ecommerce.transformed_data.dim_customers` LIMIT 10;")
        st.dataframe(df,use_container_width=True, hide_index=True)

def main():

    #Page Setup
    st.set_page_config(
        page_title="Olist E-Commerce",
        page_icon=":smile:",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    # ---- END OF SETUP ---- #

    # ---- BEGIN OF CONTENT ---- #
    pg = st.navigation([
        st.Page(home, title="Home", icon=":material/home:"),
        st.Page(dashboard, title="Dashboard", icon=":material/dashboard:"),
    ])
    pg.run()
    # ---- END OF CONTENT ---- #


if __name__ == "__main__":
    main()