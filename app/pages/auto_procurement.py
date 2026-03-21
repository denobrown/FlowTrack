import streamlit as st
import pandas as pd
from ai.auto_procurement import generate_purchase_orders

def show():

    st.title("Automated Procurement Suggestions")

    inventory = pd.read_csv("data/inventory.csv")

    orders = generate_purchase_orders(inventory)

    st.dataframe(orders)