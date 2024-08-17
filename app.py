import streamlit as st
from google.cloud import bigquery
import pandas as pd
import numpy as np
import plotly.express as px

def home():
    #Sidebar
    st.sidebar.title('Home')

def dashboard():
    #Importing Files
    df_payments = pd.read_csv("./data/raw/olist_order_payments_dataset.csv", sep=",", usecols=['order_id','payment_value'])
    df_orders = pd.read_csv("./data/raw/orders_dataset.csv", sep=",", usecols=['order_id','order_approved_at'])

    df_merged = df_orders.merge(df_payments, how="inner", on='order_id')
    df_merged['order_approved_at'] = pd.to_datetime(df_merged['order_approved_at']).dt.floor('D')
    df_merged['order_approved_at'] = df_merged['order_approved_at']
    df_sum = df_merged.groupby('order_approved_at')[['payment_value']].sum()

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
        fig = px.line(df_sum, x=df_sum.index, y="payment_value")
        st.plotly_chart(fig, key="iris")

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