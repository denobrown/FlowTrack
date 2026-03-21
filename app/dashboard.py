import streamlit as st
import pandas as pd

st.title("📊 FlowTrack Dashboard")

data = {
    "Warehouse": ["Nairobi", "Mombasa", "Kisumu"],
    "Stock Value": [150000, 230000, 120000],
}

df = pd.DataFrame(data)

st.subheader("Warehouse Inventory Overview")
st.dataframe(df)

st.bar_chart(df.set_index("Warehouse"))

st.subheader("Upcoming Shipments")

shipments = pd.DataFrame({
    "Shipment ID":[101,102,103],
    "Port of Call":["Mombasa","Durban","Shanghai"],
    "Arrival Date":["2026-04-12","2026-04-22","2026-05-01"]
})

st.table(shipments)