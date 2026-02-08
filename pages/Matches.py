import streamlit as st
from logic.matching import match_request_to_listings
from database.database import (
    get_active_requests,
    get_active_listings
)

st.set_page_config(page_title="Matches | ZERO WASTED", layout="wide")

# ---------- STYLE ----------
st.markdown("""
<style>
.card {
  background: #020617;
  border: 1px solid rgba(255,255,255,0.06);
  border-radius: 16px;
  padding: 18px;
  margin-bottom: 16px;
}
.title {
  font-size: 26px;
  font-weight: 800;
  color: #22c55e;
}
.sub {
  color: #9ca3af;
  font-size: 14px;
}
.match {
  border-left: 4px solid #22c55e;
}
.badge {
  background: #022c22;
  color: #22c55e;
  padding: 4px 10px;
  border-radius: 999px;
  font-size: 12px;
  font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown("""
<div class="card">
  <div class="title">Smart Matches</div>
  <div class="sub">
    Requests matched to nearby contributions using distance, quantity, and type.
  </div>
</div>
""", unsafe_allow_html=True)

# ---------- FETCH DATA ----------
try:
    requests = get_active_requests()
    listings = get_active_listings()
except Exception as e:
    st.error("Failed to load data from database.")
    st.caption(str(e))
    st.stop()

if not requests:
    st.info("No active requests found.")
    st.stop()

if not listings:
    st.info("No active listings available.")
    st.stop()

# ---------- SELECT REQUEST ----------
selected_index = st.selectbox(
    "Select request",
    range(len(requests)),
    format_func=lambda i: f"{requests[i]['quantity']} × {requests[i]['type']}"
)

request = requests[selected_index]
max_distance = request.get("max_distance_km", 5.0)

st.caption(f"Showing matches within {max_distance} km")

# ---------- SHOW REQUEST ----------
st.markdown(f"""
<div class="card">
  <strong>{request['quantity']} × {request['type']}</strong><br>
  <span class="sub">
    Request location: {request.get('location_label', 'Unknown')}
  </span>
</div>
""", unsafe_allow_html=True)

# ---------- MATCHING ----------
matches = match_request_to_listings(
    request,
    listings,
    max_distance_km=max_distance
)

if not matches:
    st.warning(
        f"No listings found within {max_distance} km. "
        "Try increasing your distance range."
    )
else:
    for m in matches:
        listing = m["listing"]
        dist = m["distance_km"]

        st.markdown(f"""
        <div class="card match">
          <span class="badge">{dist} km away</span><br><br>
          <strong>{listing['quantity']} × {listing['type']}</strong><br>
          <span class="sub">
            Location: {listing.get('location_label', 'Unknown')}<br>
            Message: {listing.get('message', '—')}
          </span>
        </div>
        """, unsafe_allow_html=True)

st.caption("Matches are ranked by proximity and feasibility.")
