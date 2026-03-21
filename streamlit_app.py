import streamlit as st

st.set_page_config(
    page_title="FlowTrack",
    page_icon="📦",
    layout="wide"
)

st.title("📦 FlowTrack")
st.subheader("The Smart Supply Chain Platform for Growing Businesses")

st.write(
"""
Track procurement, inventory, shipments, and supplier payments
in one powerful platform built for SMEs.
"""
)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Purchase Orders Managed", "10,000+")

with col2:
    st.metric("Warehouses Supported", "Unlimited")

with col3:
    st.metric("Real-time Shipment Visibility", "100%")

st.markdown("---")

st.header("Core Features")

features = [
"📦 Purchase Order Tracking",
"🏬 Multi-Warehouse Inventory Management",
"🚢 Shipment & Port Tracking",
"💰 Supplier Payment Monitoring",
"📊 AI Forecasting & Analytics",
"🔐 Secure Authentication with MFA"
]

for f in features:
    st.write(f)

st.markdown("---")

st.header("Why Companies Choose FlowTrack")

st.write("""
• Replace multiple spreadsheets with a single secure system  
• Gain real-time supply chain visibility  
• Reduce stockouts and overstock  
• Track supplier payments accurately  
• Improve procurement decision-making
""")

st.markdown("---")

if st.button("Request Demo"):
    st.success("Thank you! Our team will contact you.")