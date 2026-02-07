import streamlit as st
import sys
import os

# ---------- PATH SETUP ----------
sys.path.append(os.path.join(os.path.dirname(__file__), 'logic'))

try:
    from database.database import requests_col, listings_col, get_latest_listings
except Exception:
    requests_col = None
    listings_col = None
    def get_latest_listings(limit=4): return []

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="ZeroWasted",
    page_icon="♻️",
    layout="wide"
)

# ---------- GLOBAL CSS ----------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
  font-family: 'Inter', sans-serif;
}

/* Force Light Theme */
[data-testid="stAppViewContainer"] {
  background-color: #f8f9fa;
  color: #1f2937;
}

#MainMenu, footer, header {visibility: hidden;}

.hero {
  background: linear-gradient(135deg, #00b87c, #059669);
  color: white;
  padding: 3rem;
  border-radius: 18px;
  box-shadow: 0 10px 30px rgba(0,184,124,0.35);
  margin-bottom: 2.5rem;
}

.hero h1 {
  font-size: 2.4rem;
  font-weight: 800;
  margin-bottom: 0.4rem;
}

.hero p {
  opacity: 0.95;
  max-width: 520px;
}

.hero-divider {
  height: 4px;
  width: 64px;
  background: white;
  border-radius: 999px;
  margin-top: 16px;
}

.hero-stats {
  display: flex;
  gap: 2rem;
  margin-top: 2rem;
}

.hero-stat {
  background: rgba(255,255,255,0.2);
  padding: 0.9rem 1.5rem;
  border-radius: 10px;
  backdrop-filter: blur(6px);
  text-align: center;
  min-width: 120px;
}

.hero-stat h3 {
  margin: 0;
  font-size: 1.6rem;
  font-weight: 700;
}

.hero-stat span {
  font-size: 0.8rem;
  opacity: 0.9;
}

/* Score Card */
.score-card {
  background: white;
  border-radius: 20px;
  padding: 2.4rem;
  box-shadow: 0 18px 45px rgba(0,0,0,0.06);
  margin-bottom: 3rem;
  border: 1px solid #f1f5f9;
}

.circle-wrap {
  margin: 22px auto;
  width: 180px;
  height: 180px;
  border-radius: 50%;
  background: conic-gradient(#00b87c 0deg, #34d399 220deg, #e5e7eb 0deg);
  display: flex;
  align-items: center;
  justify-content: center;
}

.circle-inner {
  width: 148px;
  height: 148px;
  background: white;
  border-radius: 50%;
  text-align: center;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.score-text {
  font-size: 2.8rem;
  font-weight: 800;
  color: #00b87c;
}

.gold-star {
  position: absolute;
  background: #fbbf24;
  color: white;
  width: 44px;
  height: 44px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.3rem;
  border: 4px solid white;
  margin-top: -165px;
  margin-left: 120px;
}

.stat-row {
  display: flex;
  justify-content: space-around;
  margin-top: 2rem;
}

.stat-row h2 {
  margin: 0;
  font-size: 1.7rem;
}

.stat-row p {
  margin: 0;
  font-size: 0.85rem;
  color: #9ca3af;
}

/* Cards */
.card {
  background: white;
  border-radius: 14px;
  border: 1px solid #e5e7eb;
  overflow: hidden;
  transition: all 0.25s ease;
}

.card:hover {
  transform: translateY(-6px);
  box-shadow: 0 18px 30px rgba(0,0,0,0.08);
}

.card img {
  width: 100%;
  height: 160px;
  object-fit: cover;
}

.card-body {
  padding: 1rem;
}

.tag {
  font-size: 0.75rem;
  font-weight: 700;
  color: #00b87c;
}

/* Buttons */
div.stButton > button {
  border-radius: 12px !important;
  font-weight: 600 !important;
  padding: 0.8rem 1.2rem !important;
}

div.stButton > button[kind="primary"] {
  background: linear-gradient(135deg, #00b87c, #059669) !important;
  color: white !important;
  box-shadow: 0 10px 25px rgba(0,184,124,0.35);
}

div.stButton > button[kind="primary"]:hover {
  transform: translateY(-2px);
  box-shadow: 0 14px 35px rgba(0,184,124,0.45);
}
</style>
""", unsafe_allow_html=True)

# ---------- DATA ----------
try:
    total_listings = listings_col.count_documents({})
    total_requests = requests_col.count_documents({})
except Exception:
    total_listings = 0
    total_requests = 0

score = min(500 + total_listings * 20 + total_requests * 10, 999)

# ---------- HERO ----------
st.markdown(f"""
<div class="hero">
  <h1>Welcome back 👋</h1>
  <p>You are actively reducing waste and helping your community thrive.</p>
  <div class="hero-divider"></div>

  <div class="hero-stats">
    <div class="hero-stat">
      <h3>{total_requests}</h3>
      <span>Needs Fulfilled</span>
    </div>
    <div class="hero-stat">
      <h3>{total_listings}</h3>
      <span>Items Shared</span>
    </div>
    <div class="hero-stat">
      <h3>24</h3>
      <span>Connections</span>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ---------- SCORE ----------
st.markdown(f"""
<div class="score-card">
  <h3 style="text-align:center;">Community Score</h3>
  <p style="text-align:center; color:#6b7280;">Your sustainability impact</p>

  <div class="circle-wrap">
    <div class="gold-star">★</div>
    <div class="circle-inner">
      <div class="score-text">{score}</div>
      <div style="color:#6b7280; font-size:0.9rem;">Points</div>
    </div>
  </div>

  <div class="stat-row">
    <div>
      <h2 style="color:#00b87c;">{total_listings}</h2>
      <p>Items Contributed</p>
    </div>
    <div>
      <h2 style="color:#3b82f6;">{total_requests}</h2>
      <p>Requests Fulfilled</p>
    </div>
    <div>
      <h2 style="color:#8b5cf6;">24</h2>
      <p>Connections</p>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ---------- ACTIONS ----------
c1, c2, c3 = st.columns([1,2,1])
with c2:
    a, b = st.columns(2)
    with a:
        st.button("➕ Contribute Surplus", type="primary", use_container_width=True)
    with b:
        st.button("📩 Request Help", use_container_width=True)

# ---------- GRID ----------
st.markdown("### 🎁 Available Surplus")
st.write("")

items = get_latest_listings(4)

if not items:
    st.info("No surplus items available right now.")
else:
    cols = st.columns(4)
    for i, item in enumerate(items):
        with cols[i % 4]:
            title = item.get("item_name", "Surplus Item")
            desc = item.get("description", "Available for pickup")
            img = item.get("image", "https://images.unsplash.com/photo-1596461404969-9ae70f2830c1?w=400&q=80")

            st.markdown(f"""
            <div class="card">
              <img src="{img}">
              <div class="card-body">
                <strong>{title}</strong>
                <p style="font-size:0.85rem; color:#6b7280;">{desc[:50]}...</p>
                <div style="display:flex; justify-content:space-between;">
                  <span class="tag">FREE</span>
                  <span style="font-size:0.75rem; color:#9ca3af;">Nearby</span>
                </div>
              </div>
            </div>
            """, unsafe_allow_html=True)

            st.button("Claim", key=f"claim_{i}", use_container_width=True)

# ---------- FOOTER ----------
st.markdown("""
<br><br>
<div style="background:#eef2ff; border-radius:16px; padding:2rem; display:flex; justify-content:space-around;">
  <div><h2 style="color:#4f46e5;">247</h2><small>Needs Fulfilled</small></div>
  <div><h2 style="color:#4f46e5;">189</h2><small>Items Shared</small></div>
</div>
""", unsafe_allow_html=True)
