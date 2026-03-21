import streamlit as st
import pandas as pd
from ai.supplier_risk import risk_score

def show():

    st.title("Supplier Risk Analysis")

    data = pd.DataFrame({
        "supplier":["ABC","Global","EastTrade"],
        "payment_delay":[5,12,2],
        "shipment_delay":[1,7,0]
    })

    scored = risk_score(data)

    st.dataframe(scored)