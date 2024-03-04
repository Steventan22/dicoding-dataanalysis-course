import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df_sales = pd.read_csv('df_sales.csv')  

def plot_customer_orders_by_location():
    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(36, 15))
    colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

    customer_orders_by_city = df_sales.groupby(by="customer_city").customer_id.nunique().sort_values(ascending=False).reset_index()

    sns.barplot(x="customer_city", y="customer_id", data=customer_orders_by_city.head(7), palette=colors, ax=ax[0])
    ax[0].set_ylabel(None)
    ax[0].set_xlabel(None)
    ax[0].tick_params(axis='x', labelrotation=45)
    ax[0].set_title("Kota", loc="center", fontsize=40)
    ax[0].tick_params(axis='y', labelsize=30)

    customer_orders_by_state = df_sales.groupby(by="customer_state").customer_id.nunique().sort_values(ascending=False).reset_index()

    sns.barplot(x="customer_state", y="customer_id", data=customer_orders_by_state.head(7), palette=colors, ax=ax[1])
    ax[1].set_ylabel(None)
    ax[1].set_xlabel(None)
    ax[1].tick_params(axis='x', labelrotation=45)
    ax[1].set_title("Negara", loc="center", fontsize=40)
    ax[1].tick_params(axis='y', labelsize=30)

    plt.suptitle("Jumlah Pesanan Pelanggan Kota dan Negara", fontsize=55)
    st.pyplot(fig)

def plot_product_performance():
    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(36, 15))
    colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

    top_product_orders = df_sales.groupby(df_sales["product_category_name_english"])["payment_value"].sum().reset_index().sort_values("payment_value", ascending=False).head(7)

    sns.barplot(x="payment_value", y="product_category_name_english", data=top_product_orders, palette=colors, ax=ax[0])
    ax[0].set_xlabel(None)
    ax[0].set_ylabel(None)
    ax[0].set_title("Best Performing Product", loc="center", fontsize=40)
    ax[0].tick_params(axis='y', labelsize=30)

    low_product_orders = df_sales.groupby(df_sales["product_category_name_english"])["payment_value"].sum().reset_index().sort_values("payment_value", ascending=True).head(7)

    sns.barplot(x="payment_value", y="product_category_name_english", data=low_product_orders, palette=colors, ax=ax[1])
    ax[1].set_xlabel(None)
    ax[1].set_ylabel(None)
    ax[1].invert_xaxis()
    ax[1].yaxis.set_label_position("right")
    ax[1].yaxis.tick_right()
    ax[1].set_title("Worst Performing Product", loc="center", fontsize=40)
    ax[1].tick_params(axis='y', labelsize=30)

    plt.suptitle("Best and Worst Performing Product by Number of Revenue", fontsize=55)
    st.pyplot(fig)

st.title('Dashboard E-commerce Sales ')
tab1, tab2 = st.tabs(["Customer Orders by Location", "Product Performance"])

with tab1:
    st.header("Customer Orders by Location")
    plot_customer_orders_by_location()

with tab2:
    st.header("Product Performance")
    plot_product_performance()