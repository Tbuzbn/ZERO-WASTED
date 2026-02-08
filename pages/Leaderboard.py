import streamlit as st

st.set_page_config(
    page_title="Leaderboard | ZERO WASTED",
    layout="centered"
)

# ---------- STYLE ----------
st.markdown("""
<style>
body {
  background-color: #020617;
}

.header {
  margin-bottom: 28px;
}

.header h1 {
  font-size: 34px;
  font-weight: 900;
  color: #22c55e;
  margin-bottom: 4px;
}

.header p {
  color: #9ca3af;
  font-size: 15px;
}

.card {
  background: #020617;
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 18px;
  padding: 18px 22px;
  margin-bottom: 14px;
  transition: transform 0.2s ease;
}

.card:hover {
  transform: translateY(-2px);
}

.top {
  border-left: 6px solid #22c55e;
}

.row {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.left {
  display: flex;
  align-items: center;
  gap: 14px;
}

.logo {
  width: 42px;
  height: 42px;
  border-radius: 50%;
  object-fit: cover;
  border: 2px solid rgba(255,255,255,0.1);
}

.rank {
  font-size: 12px;
  letter-spacing: 1px;
  color: #9ca3af;
  font-weight: 700;
}

.name {
  font-size: 20px;
  font-weight: 800;
  color: white;
}

.score {
  font-size: 22px;
  font-weight: 900;
  color: #22c55e;
}
</style>
""", unsafe_allow_html=True)

# ---------- DATA ----------
INDIVIDUALS = [
    {
        "name": "Aarav",
        "score": 120,
        "logo": "https://api.dicebear.com/7.x/initials/svg?seed=A"
    },
    {
        "name": "Meera",
        "score": 95,
        "logo": "https://api.dicebear.com/7.x/initials/svg?seed=M"
    },
    {
        "name": "Rahul (YOU)",
        "score": 80,
        "logo": "https://api.dicebear.com/7.x/initials/svg?seed=R"
    },
    {
        "name": "Sneha",
        "score": 60,
        "logo": "https://api.dicebear.com/7.x/initials/svg?seed=S"
    },
]

ORGS = [
    {
        "name": "GreenMart",
        "score": 420,
        "logo": "https://cdn-icons-png.flaticon.com/512/2909/2909763.png"
    },
    {
        "name": "Food4All NGO",
        "score": 350,
        "logo": "https://cdn-icons-png.flaticon.com/512/1046/1046784.png"
    },
    {
        "name": "EcoShip",
        "score": 290,
        "logo": "https://cdn-icons-png.flaticon.com/512/565/565547.png"
    },
]


# ---------- HEADER ----------
st.markdown("""
<div class="header">
  <h1>Impact Leaders</h1>
  <p>Top contributors driving real community change this week</p>
</div>
""", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["👤 Individuals", "🏢 Organizations"])

# ---------- INDIVIDUALS ----------
with tab1:
    for i, u in enumerate(INDIVIDUALS):
        cls = "card top" if i == 0 else "card"
        st.markdown(f"""
        <div class="{cls}">
          <div class="row">
            <div class="left">
              <img src="{u['logo']}" class="logo"/>
              <div>
                <div class="rank">RANK {i+1}</div>
                <div class="name">{u['name']}</div>
              </div>
            </div>
            <div class="score">{u['score']} pts</div>
          </div>
        </div>
        """, unsafe_allow_html=True)

# ---------- ORGANIZATIONS ----------
with tab2:
    for i, o in enumerate(ORGS):
        cls = "card top" if i == 0 else "card"
        st.markdown(f"""
        <div class="{cls}">
          <div class="row">
            <div class="left">
              <img src="{o['logo']}" class="logo"/>
              <div>
                <div class="rank">RANK {i+1}</div>
                <div class="name">{o['name']}</div>
              </div>
            </div>
            <div class="score">{o['score']} pts</div>
          </div>
        </div>
        """, unsafe_allow_html=True)

# ---------- FOOTER ----------
st.caption("Leaderboard resets weekly. Consistent impact is what counts.")
