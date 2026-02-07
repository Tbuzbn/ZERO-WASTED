import streamlit as st

st.title("Request Resource")
st.caption("Request resources available in your area")

# ---------- RESOURCE DETAILS ----------
resource_type = st.selectbox(
    "Resource Type Needed",
    ["Food", "Books", "Clothing", "Other"]
)

quantity = st.number_input(
    "Quantity Needed",
    min_value=1,
    step=1
)

# ---------- OPTIONAL MESSAGE ----------
request_message = st.text_area(
    "Optional Message to Contributor",
    placeholder="Any context that might help with matching (timing, constraints, purpose, etc.)",
    height=100
)

# ---------- LOCATION ----------
st.subheader("Location")

st.info(
    "Your location will be detected automatically using maps "
    "to calculate distance and estimated travel time."
)

if st.button("Detect My Location"):
    st.success("Location detected successfully (mock).")

# ---------- REQUESTER TYPE ----------
requester_type = st.radio(
    "Requester Type",
    ["Individual", "NGO"]
)

# ---------- SUBMIT ----------
st.button("Submit Request")
