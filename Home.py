import streamlit as st

st.set_page_config(
    page_title="ZERO WASTED",
    layout="wide"
)

st.title("ZERO WASTED")
st.caption("Turning surplus into shared impact")

st.write("")

left, right = st.columns([3, 1])
with right:
    st.metric("Community Score", "—")

st.subheader("Your Lifetime Impact")

c1, c2, c3 = st.columns(3)
c1.metric("Resources Shared", "—")
c2.metric("People Helped", "—")
c3.metric("CO₂ Saved (kg)", "—")

st.subheader("Community Impact")

d1, d2, d3 = st.columns(3)
d1.metric("Total Listings", "—")
d2.metric("Total Requests Fulfilled", "—")
d3.metric("Total CO₂ Saved (kg)", "—")

st.write("")
center = st.columns([2, 2, 2])
with center[1]:
    st.button("➕ Contribute Resource")
    st.write("")
    st.button("📦 Request Resource")
