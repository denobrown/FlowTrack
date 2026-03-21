import streamlit as st

st.title("🔐 FlowTrack Login")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if username == "admin" and password == "password":
        st.success("Login Successful")
        st.switch_page("dashboard.py")
    else:
        st.error("Invalid credentials")