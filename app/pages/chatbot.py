import streamlit as st
import pandas as pd
from ai.chatbot import answer_query

def show():

    st.title("Supply Chain AI Assistant")

    orders = pd.read_csv("data/purchase_orders.csv")
    inventory = pd.read_csv("data/inventory.csv")

    question = st.text_input("Ask a question about your supply chain")

    if question:

        response = answer_query(question, orders, inventory)

        st.write(response)