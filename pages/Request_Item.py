import streamlit as st
from datetime import datetime, timezone
from database.database import add_request
from logic.location_picker import detect_location, location_display

st.set_page_config(page_title="Request | ZERO WASTED", layout="centered")

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
st.session_state.setdefault("last_request", None)
st.session_state.setdefault("request_location_label", "")
st.session_state.setdefault("request_location_coords", None)

# ---------- HEADER ----------
st.markdown("""
<div class="card">
  <div class="title">Request a Resource</div>
  <div class="desc">
    Ask for resources available in your local community.
  </div>
</div>
""", unsafe_allow_html=True)

# ---------- LOCATION (OUTSIDE FORM) ----------
st.markdown("""
<div class="card">
  <div class="title" style="font-size:22px;">Location</div>
  <div class="desc">
    Used to find nearby contributions. Exact coordinates are never shown publicly.
  </div>
</div>
""", unsafe_allow_html=True)

# Detect + show location
detect_location("request_location")
location_display("request_location")

# ---------- FORM ----------
with st.form("request_form"):
    st.markdown("""
    <div class="card">
      <div class="title" style="font-size:22px;">Request Details</div>
    """, unsafe_allow_html=True)

    resource_type = st.selectbox(
        "Resource Type Needed",
        ["Food", "Books", "Clothing", "Other"]
    )

    quantity = st.number_input(
        "Quantity Needed",
        min_value=1,
        step=1
    )

    # Auto-filled location field
    location_label = st.text_input(
        "Area / Locality",
        value=st.session_state.get("request_location_label", ""),
        placeholder="Lat, Lng will appear after detection"
    )

    request_message = st.text_area(
        "Optional Message to Contributor",
        placeholder="Any context that might help with matching",
        height=110
    )

    requester_type = st.radio(
        "Requester Type",
        ["Individual", "NGO"]
    )

    submitted = st.form_submit_button("📨 Submit Request")

    st.markdown("</div>", unsafe_allow_html=True)

# ---------- SUBMIT LOGIC ----------
if submitted:
    if st.session_state.get("request_location_coords") is None:
        st.error("Please detect your location before submitting.")
        st.stop()

    final_label = (
        location_label
        or st.session_state["request_location_label"]
        or "Unknown location"
    )

    payload = {
        "type": resource_type,
        "quantity": int(quantity),
        "message": request_message.strip(),
        "requester_type": requester_type,
        "location_label": final_label,
        "location": st.session_state["request_location_coords"],
        "created_at": datetime.now(timezone.utc),
        "status": "active"
    }

    try:
        add_request(payload)
        st.session_state.last_request = payload
        st.success("Your request has been submitted!")
        st.toast("Nearby contributors will be notified 🌱")
    except Exception as e:
        st.error("Something went wrong while submitting the request.")
        st.caption(str(e))

# ---------- CONFIRMATION ----------
if st.session_state.last_request:
    data = st.session_state.last_request

    st.markdown(f"""
    <div class="card" style="border-left:4px solid #3b82f6;">
      <div class="title" style="font-size:20px;">Request Summary</div>
      <div class="desc">
        <strong>{data['quantity']} × {data['type']}</strong><br>
        Requested by: {data['requester_type']}<br>
        Location: {data['location_label']}<br>
        Message: {data['message'] or "No message provided"}
      </div>
    </div>
    """, unsafe_allow_html=True)

# ---------- FOOTER ----------
st.caption("Requests are matched based on proximity, availability, and urgency.")
