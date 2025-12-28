import streamlit as st
import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt

# ----------------------
# Page Config
# ----------------------
st.set_page_config(
    page_title="Sales Dashboard",
    page_icon="📊",
    layout="wide"
)

# ----------------------
# Title
# ----------------------
st.title("📊 Sales Dashboard")
st.markdown("### Streamlit Dashboard Example")

# ----------------------
# Generate Sample Data
# ----------------------
np.random.seed(42)

data = pd.DataFrame({
    "Date": pd.date_range(start="2024-01-01", periods=30),
    "Sales": np.random.randint(200, 1000, 30),
    "Profit": np.random.randint(50, 400, 30),
    "Category": np.random.choice(["Electronics", "Fashion", "Food"], 30)
})

# ----------------------
# Sidebar Filters
# ----------------------
st.sidebar.header("🔍 Filters")

category_filter = st.sidebar.multiselect(
    "Select Category",
    options=data["Category"].unique(),
    default=data["Category"].unique()
)

filtered_data = data[data["Category"].isin(category_filter)]

# ----------------------
# KPIs
# ----------------------
col1, col2, col3 = st.columns(3)

col1.metric("💰 Total Sales", f"{filtered_data['Sales'].sum():,}")
col2.metric("📈 Total Profit", f"{filtered_data['Profit'].sum():,}")
col3.metric("📦 Orders", filtered_data.shape[0])

# ----------------------
# Charts
# ----------------------
# col4, col5 = st.columns(2)

# with col4:
#     st.subheader("Sales Over Time")
#     fig, ax = plt.subplots()
#     ax.plot(filtered_data["Date"], filtered_data["Sales"])
#     ax.set_xlabel("Date")
#     ax.set_ylabel("Sales")
#     st.pyplot(fig)

# with col5:
#     st.subheader("Sales by Category")
#     category_sales = filtered_data.groupby("Category")["Sales"].sum()
#     fig2, ax2 = plt.subplots()
#     ax2.bar(category_sales.index, category_sales.values)
#     ax2.set_ylabel("Sales")
#     st.pyplot(fig2)

# ----------------------
# Data Table
# ----------------------
st.subheader("📄 Raw Data")
st.dataframe(filtered_data)

