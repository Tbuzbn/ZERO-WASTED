import streamlit as st

st.set_page_config(layout="wide")

# ---------- HEADER ----------
st.markdown(
    """
    <h1 style='margin-bottom: 0;'>Community Perks</h1>
    <p style='color: gray; margin-top: 0;'>
    Rewards unlocked through meaningful contributions
    </p>
    """,
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

# ---------- USER SCORE ----------
user_score = 1280  # demo placeholder

score_col, _ = st.columns([1, 3])
with score_col:
    st.metric("Your Community Score", user_score)

st.markdown("<br>", unsafe_allow_html=True)

# ---------- EXPLANATION ----------
st.info(
    "Community Perks are benefits offered by partner companies as part of their "
    "Corporate Social Responsibility (CSR) initiatives. "
    "Higher contributions unlock better rewards."
)

st.markdown("<br>", unsafe_allow_html=True)

# ---------- PERKS GRID ----------
st.subheader("Partner Offers")

col1, col2 = st.columns(2)

def perk_card(company, offer, required_score, unlocked):
    # Create a safe, unique base key
    base_key = company.replace(" ", "").replace("🛒", "").replace("📦", "").replace("☕", "").replace("🧴", "").lower()

    with st.container():
        st.markdown(f"### {company}")
        st.write(f"**Offer:** {offer}")
        st.write(f"**Required Score:** {required_score}")

        if unlocked:
            st.success("Unlocked")
            st.button(
                "Redeem",
                disabled=True,
                key=f"{base_key}_redeem"
            )
        else:
            st.warning("Locked")
            st.button(
                "Locked",
                disabled=True,
                key=f"{base_key}_locked"
            )

        st.markdown("<hr>", unsafe_allow_html=True)



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
    "Perks are provided by partner organizations to encourage sustainable behavior "
    "and community-driven impact."
)
