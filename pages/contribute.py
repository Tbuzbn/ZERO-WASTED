import streamlit as st

st.title("Contribute Resource")
st.caption("Share surplus resources with the community")

# ---------- RESOURCE DETAILS ----------
resource_type = st.selectbox(
    "Resource Type",
    ["Food", "Books", "Clothing", "Other"]
)

quantity = st.number_input(
    "Quantity",
    min_value=1,
    step=1
)

# ---------- OPTIONAL MESSAGE ----------
message = st.text_area(
    "Optional Message to Recipient",
    placeholder="Any details the recipient should know (pickup time, condition, etc.)",
    height=100
)

# ---------- LOCATION ----------
st.subheader("Location")

st.info(
    "Your location will be detected automatically to help match "
    "your listing efficiently."
)

if st.button("Detect My Location"):
    st.success("Location detected successfully (mock).")

# ---------- SUBMIT ----------
st.button("Submit Listing")
