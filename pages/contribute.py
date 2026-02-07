import streamlit as st
from datetime import datetime, timezone
from database.database import add_listing
from logic.location_picker import detect_location, location_display, location_input

st.set_page_config(page_title="Contribute | ZERO WASTED", layout="centered")

# ---------- THEME ----------
ACCENT = "#22c55e"
MUTED = "#9ca3af"

# ---------- GLOBAL STYLE ----------
st.markdown("""
<style>
.card {
  background: #020617;
  border: 1px solid rgba(255,255,255,0.06);
  border-radius: 18px;
  padding: 22px;
  margin-bottom: 18px;
}
.title {
  font-size: 28px;
  font-weight: 800;
  color: #22c55e;
}
.desc {
  font-size: 15px;
  color: #9ca3af;
}
</style>
""", unsafe_allow_html=True)

# ---------- SESSION STATE ----------
st.session_state.setdefault("last_submission", None)
st.session_state.setdefault("contribute_location_label", "")
st.session_state.setdefault("contribute_location_coords", None)

# ---------- HEADER ----------
st.markdown("""
<div class="card">
  <div class="title">Contribute a Resource</div>
  <div class="desc">
    Share surplus resources with your local community in minutes.
  </div>
</div>
""", unsafe_allow_html=True)

# ---------- LOCATION (OUTSIDE FORM) ----------
st.markdown("""
<div class="card">
  <div class="title" style="font-size:22px;">Location</div>
  <div class="desc">
    Used only to match your contribution with nearby requests.
    Exact coordinates are never shown publicly.
  </div>
</div>
""", unsafe_allow_html=True)

# Detect + display location
detect_location("contribute_location")
location_display("contribute_location")

# ---------- FORM ----------
with st.form("contribute_form"):
    st.markdown("""
    <div class="card">
      <div class="title" style="font-size:22px;">Resource Details</div>
    """, unsafe_allow_html=True)

    resource_type = st.selectbox(
        "Resource Type",
        ["Food", "Books", "Clothing", "Other"]
    )

    quantity = st.number_input(
        "Quantity",
        min_value=1,
        step=1
    )

    message = st.text_area(
        "Optional message to recipient",
        placeholder="Pickup time, condition, storage instructions, etc.",
        height=110
    )

    # Editable label synced with detected location
    location_label = st.text_input(
        "Area / Locality",
        value=st.session_state.get("contribute_location_label", ""),
        placeholder="Lat, Lng will appear after detection"
    )    

    final_label = (
        location_label
        or st.session_state["contribute_location_label"]
        or "Unknown location"
    )

    submitted = st.form_submit_button("🚀 Publish Listing")

    st.markdown("</div>", unsafe_allow_html=True)

# ---------- SUBMIT LOGIC ----------
if submitted:
    if st.session_state["contribute_location_coords"] is None:
        st.error("Please detect your location before submitting.")
        st.stop()

    final_label = (
        location_label
        or st.session_state["contribute_location_label"]
        or "Unknown area"
    )

    payload = {
        "type": resource_type,
        "quantity": int(quantity),
        "message": message.strip(),
        "location_label": final_label,
        "location": st.session_state["contribute_location_coords"],
        "created_at": datetime.now(timezone.utc),
        "status": "active"
    }

    try:
        add_listing(payload)
        st.session_state.last_submission = payload
        st.success("Your contribution has been published!")
        st.toast("Thanks for contributing to ZERO WASTED 🌱")
    except Exception as e:
        st.error("Something went wrong while publishing the listing.")
        st.caption(str(e))

# ---------- CONFIRMATION ----------
if st.session_state.last_submission:
    data = st.session_state.last_submission

    st.markdown(f"""
    <div class="card" style="border-left:4px solid {ACCENT};">
      <div class="title" style="font-size:20px;">Submission Summary</div>
      <div class="desc">
        <strong>{data['quantity']} × {data['type']}</strong><br>
        Location: {data['location_label']}<br>
        Message: {data['message'] or "No message provided"}
      </div>
    </div>
    """, unsafe_allow_html=True)

# ---------- FOOTER ----------
st.caption("Every contribution increases your Community Score and unlocks rewards.")
