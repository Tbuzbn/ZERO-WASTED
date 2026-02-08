import streamlit as st

st.set_page_config(layout="wide", page_title="Community Perks | ZERO WASTED")

# ---------- THEME ----------
ACCENT = "#22c55e"
MUTED = "#9ca3af"
CARD_BG = "#020617"
BORDER = "rgba(255,255,255,0.06)"
SHADOW = "0 16px 40px rgba(0,0,0,0.35)"

# ---------- STYLE ----------
st.markdown("""
<style>
.perk-card {
  background: #020617;
  border: 1px solid rgba(255,255,255,0.06);
  border-radius: 18px;
  padding: 22px;
  box-shadow: 0 16px 40px rgba(0,0,0,0.35);
  margin-bottom: 20px;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}
.perk-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 22px 55px rgba(0,0,0,0.45);
}
.perk-title {
  font-size: 22px;
  font-weight: 800;
  color: #22c55e;
}
.perk-offer {
  font-size: 15px;
  margin-top: 6px;
}
.perk-meta {
  font-size: 13px;
  color: #9ca3af;
  margin-top: 10px;
}
.badge-unlocked {
  display: inline-block;
  background: rgba(34,197,94,0.15);
  color: #22c55e;
  padding: 4px 10px;
  border-radius: 999px;
  font-size: 12px;
  font-weight: 700;
}
.badge-locked {
  display: inline-block;
  background: rgba(239,68,68,0.15);
  color: #ef4444;
  padding: 4px 10px;
  border-radius: 999px;
  font-size: 12px;
  font-weight: 700;
}
.hero {
  background: linear-gradient(135deg, #022c22, #020617);
  border-radius: 22px;
  padding: 30px;
  border: 1px solid rgba(255,255,255,0.06);
  margin-bottom: 28px;
}
.hero h1 {
  margin: 0;
  font-size: 34px;
  color: #22c55e;
}
.hero p {
  margin-top: 6px;
  color: #9ca3af;
}
</style>
""", unsafe_allow_html=True)

# ---------- HERO ----------
st.markdown("""
<div class="hero">
  <h1>Community Perks</h1>
  <p>Real rewards unlocked through real impact 🌍</p>
</div>
""", unsafe_allow_html=True)

# ---------- USER SCORE ----------
user_score = 1280  # demo placeholder

c1, c2 = st.columns([1, 3])
with c1:
    st.metric("Your Community Score", user_score)

st.markdown("<br>", unsafe_allow_html=True)

# ---------- INFO ----------
st.info(
    "Community Perks are offered by partner companies as part of their CSR initiatives. "
    "Contribute more, unlock better rewards."
)

st.markdown("<br>", unsafe_allow_html=True)

# ---------- PERKS ----------
st.subheader("🤝 Partner Offers")

def perk_card(company, offer, required_score, unlocked):
    base_key = company.encode("utf-8").hex()  # bulletproof unique key

    st.markdown(f"""
    <div class="perk-card">
      <div class="perk-title">{company}</div>
      <div class="perk-offer"><strong>{offer}</strong></div>
      <div class="perk-meta">Required Score: {required_score}</div>
      <br>
      {"<span class='badge-unlocked'>Unlocked</span>" if unlocked else "<span class='badge-locked'>Locked</span>"}
    </div>
    """, unsafe_allow_html=True)

    if unlocked:
        st.button("🎁 Redeem Reward", key=f"{base_key}_redeem")
    else:
        st.button("🔒 Locked", disabled=True, key=f"{base_key}_locked")


col1, col2 = st.columns(2)

with col1:
    perk_card(
        company="🛒 FreshMart",
        offer="15% off groceries",
        required_score=1000,
        unlocked=user_score >= 1000
    )

    perk_card(
        company="📦 EcoShip",
        offer="Free delivery on next order",
        required_score=1500,
        unlocked=user_score >= 1500
    )

with col2:
    perk_card(
        company="☕ GreenBrew",
        offer="Buy 1 Get 1 Free",
        required_score=800,
        unlocked=user_score >= 800
    )

    perk_card(
        company="🧴 RefillCo",
        offer="20% off refill packs",
        required_score=2000,
        unlocked=user_score >= 2000
    )

# ---------- FOOTER ----------
st.markdown("<br>", unsafe_allow_html=True)
st.caption(
    "Perks are provided by partner organizations to incentivize sustainability and community impact."
)
