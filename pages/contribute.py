import streamlit as st
from datetime import datetime
from database.database import add_listing


st.set_page_config(page_title="Contribute | ZERO WASTED", layout="centered")

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
st.session_state.setdefault("last_submission", None)

# ---------- HEADER ----------
st.markdown("""
<div class="card">
  <div class="title">Contribute a Resource</div>
  <div class="desc">
    Share surplus resources with your local community in minutes.
  </div>
</div>
""", unsafe_allow_html=True)

# ---------- LOCATION ----------
st.markdown("""
<div class="card">
  <div class="title" style="font-size:22px;">Location</div>
  <div class="desc">
    Used only to match your contribution with nearby requests.
    Exact coordinates are never shown publicly.
  </div>
""", unsafe_allow_html=True)

if st.button("📍 Detect My Location"):
    st.session_state.location_detected = True

if st.session_state.location_detected:
    st.success("Location detected successfully (demo).")

st.markdown("</div>", unsafe_allow_html=True)

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

    location_label = st.text_input(
        "Visible location label (city / area)",
        placeholder="e.g. Indiranagar, Bengaluru"
    )

    submitted = st.form_submit_button("🚀 Publish Listing")

    st.markdown("</div>", unsafe_allow_html=True)
    
# ---------- DYNAMIC CONFIRMATION ----------
    if submitted:
        payload = {
            "type": resource_type,
            "quantity": int(quantity),
            "message": message.strip(),
            "location_label": location_label.strip(),
            "created_at": datetime.utcnow(),
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

if "last_submission" in st.session_state and st.session_state.last_submission:
    data = st.session_state.last_submission

    st.markdown(f"""
    <div class="card" style="border-left:4px solid {ACCENT};">
      <div class="title" style="font-size:20px;">Submission Summary</div>
      <div class="desc">
        <strong>{data['quantity']} × {data['type']}</strong><br>
        Location: {data['location_label'] or "Not specified"}<br>
        Message: {data['message'] or "No message provided"}
      </div>
    </div>
    """, unsafe_allow_html=True)

# ---------- FOOTER ----------
st.caption("Every contribution increases your Community Score and unlocks rewards.")


