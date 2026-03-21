import streamlit as st
import pandas as pd
import pydeck as pdk

def show():

    st.title("Global Container Shipping Routes")

    routes = pd.DataFrame({
        "lat":[25.2048,1.3521,-4.0435],
        "lon":[55.2708,103.8198,39.6682],
        "port":[
            "Dubai",
            "Singapore",
            "Mombasa"
        ]
    })

    layer = pdk.Layer(
        "ScatterplotLayer",
        data=routes,
        get_position='[lon, lat]',
        get_radius=50000,
        pickable=True
    )

    view = pdk.ViewState(
        latitude=10,
        longitude=60,
        zoom=2
    )

    deck = pdk.Deck(layers=[layer], initial_view_state=view)

    st.pydeck_chart(deck)