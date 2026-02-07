import streamlit as st

st.set_page_config(page_title="Request | ZERO WASTED", layout="centered")

# ---------- THEME ----------
ACCENT = "#22c55e"
MUTED = "#9ca3af"
CARD_BG = "#020617"
BORDER = "rgba(255,255,255,0.06)"
SHADOW = "0 16px 40px rgba(0,0,0,0.35)"

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
        st.session_state.last_request = {
            "resource_type": resource_type,
            "quantity": quantity,
            "requester_type": requester_type,
            "message": request_message
        }

        st.success("Your request has been submitted!")
        st.toast("Your request is now visible to nearby contributors 🌱")

# ---------- DYNAMIC CONFIRMATION ----------
if st.session_state.last_request:
    data = st.session_state.last_request

    st.markdown(f"""
    <div class="card" style="border-left:4px solid {ACCENT};">
      <div class="title" style="font-size:20px;">Request Summary</div>
      <div class="desc">
        <strong>{data['quantity']} × {data['resource_type']}</strong><br>
        Requester Type: {data['requester_type']}<br>
        Message: {data['message'] or "No message provided"}
      </div>
    </div>
    """, unsafe_allow_html=True)

# ---------- FOOTER ----------
st.caption("Requests are matched based on proximity, availability, and urgency.")
