import streamlit as st
from datetime import datetime
from database.database import get_total_listings
    

st.set_page_config(page_title="My Listings | ZERO WASTED", layout="wide")

# ---------- THEME ----------
st.markdown("""
<style>
.card {
  background: white;
  border-radius: 16px;
  padding: 1.5rem;
  border: 1px solid #e5e7eb;
  box-shadow: 0 10px 25px rgba(0,0,0,0.05);
  margin-bottom: 1rem;
}
.title {
  font-size: 1.8rem;
  font-weight: 800;
  color: #00b87c;
}
.meta {
  font-size: 0.85rem;
  color: #6b7280;
}
.badge {
  background: #ecfdf5;
  color: #059669;
  padding: 4px 10px;
  border-radius: 999px;
  font-size: 0.75rem;
  font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown("""
<div class="card">
  <div class="title">My Active Listings</div>
  <div class="meta">
    Resources you’ve shared with the community
  </div>
</div>
""", unsafe_allow_html=True)

# ---------- FETCH DATA ----------
try:
    listings = get_active_listings(limit=20)
except Exception as e:
    listings = []
    st.error("Could not fetch listings from database.")
    st.caption(str(e))

# ---------- EMPTY STATE ----------
if not listings:
    st.info("You have no active listings right now.")
else:
    for item in listings:
        created = item.get("created_at")
        created_str = (
            created.strftime("%d %b %Y, %H:%M")
            if isinstance(created, datetime)
            else "Unknown time"
        )

        st.markdown(f"""
        <div class="card">
          <div style="display:flex; justify-content:space-between; align-items:center;">
            <strong>{item.get("quantity", "?")} × {item.get("type", "Item")}</strong>
            <span class="badge">Active</span>
          </div>

          <div class="meta" style="margin-top:6px;">
            Location: {item.get("location_label", "Not specified")} <br>
            Posted: {created_str}
          </div>

          <div style="margin-top:10px;">
            {item.get("message", "No message provided")}
          </div>
        </div>
        """, unsafe_allow_html=True)
