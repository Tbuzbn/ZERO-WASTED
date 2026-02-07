import streamlit as st
from datetime import datetime

try:
    from logic.database.database import add_request
except ImportError:
    from database.database import add_request

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
  box-shadow: 0 16px 40px rgba(0,0,0,0.35);
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

# ---------- STATE ----------
st.session_state.setdefault("location_detected", False)
st.session_state.setdefault("last_request", None)

# ---------- HEADER ----------
st.markdown("""
<div class="card">
  <div class="title">Request a Resource</div>
  <div class="desc">
    Ask for resources available in your local community.
  </div>
</div>
""", unsafe_allow_html=True)

# ---------- LOCATION ----------
st.markdown("""
<div class="card">
  <div class="title" style="font-size:22px;">Location</div>
  <div class="desc">
    Used to find nearby contributions. Exact coordinates are never shown publicly.
  </div>
""", unsafe_allow_html=True)

if st.button("📍 Detect My Location"):
    st.session_state.location_detected = True

if st.session_state.location_detected:
    st.success("Location detected successfully (demo).")

st.markdown("</div>", unsafe_allow_html=True)

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

    location_label = st.text_input(
        "Visible Location (city / area)",
        placeholder="e.g. Indiranagar, Bengaluru"
    )

    request_message = st.text_area(
        "Optional Message to Contributor",
        placeholder="Any context that might help with matching (timing, purpose, constraints, etc.)",
        height=110
    )

    requester_type = st.radio(
        "Requester Type",
        ["Individual", "NGO"]
    )

    submitted = st.form_submit_button("📨 Submit Request")

    st.markdown("</div>", unsafe_allow_html=True)

    if submitted:
        payload = {
            "type": resource_type,
            "quantity": int(quantity),
            "message": request_message.strip(),
            "requester_type": requester_type,
            "location_label": location_label.strip(),
            "created_at": datetime.utcnow(),
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
if "last_request" in st.session_state and st.session_state.last_request:
    data = st.session_state.last_request

    st.markdown("""
    <div class="card" style="border-left:4px solid #3b82f6;">
      <div class="title" style="font-size:20px;">Request Summary</div>
      <div class="desc">
        <strong>{qty} × {rtype}</strong><br>
        Requested by: {who}<br>
        Location: {loc}<br>
        Message: {msg}
      </div>
    </div>
    """.format(
        qty=data["quantity"],
        rtype=data["type"],
        who=data["requester_type"],
        loc=data["location_label"] or "Not specified",
        msg=data["message"] or "No message provided"
    ), unsafe_allow_html=True)

# ---------- FOOTER ----------
st.caption("Requests are matched based on proximity, availability, and urgency.")
