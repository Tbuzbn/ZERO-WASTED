import streamlit as st
from logic.community_score import lol   # works now

st.title("ZERO WASTED")

st.metric("Community Score", lol())

st.subheader("Lifetime Stats")

col1, col2, col3 = st.columns(3)
col1.metric("Resources Shared", "24")
col2.metric("People Helped", "68")
col3.metric("CO₂ Saved", "142 kg")

st.write("")

center = st.columns([2, 2, 2])
with center[1]:
    st.button("➕ Add Listing")
    st.write("")
    st.button("📦 Request Resource")
