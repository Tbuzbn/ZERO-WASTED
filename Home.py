import streamlit as st

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        background-color: #f8f9fa;
        color: #1f2937;
    }
    
    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Banner */
    .hero-banner {
        background: linear-gradient(135deg, #00b87c 0%, #059669 100%);
        color: white;
        padding: 2rem;
        border-radius: 16px;
        margin-bottom: 2rem;
    }

    /* Card Styling */
    .need-card {
        background: white;
        border: 1px solid #e5e7eb;
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        transition: transform 0.2s, box-shadow 0.2s;
        height: 100%; /* Important for grid alignment */
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    .need-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
    }

    .user-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 1rem;
    }
    .user-info {
        display: flex;
        gap: 10px;
        align-items: center;
    }
    .avatar {
        width: 40px; height: 40px; border-radius: 50%; object-fit: cover;
    }
    .badge {
        background-color: #fee2e2; color: #ef4444;
        padding: 4px 10px; border-radius: 20px; font-size: 0.75rem; font-weight: 600;
    }
    .verified {
        color: #00b87c; font-size: 0.85rem; display: flex; align-items: center; gap: 4px;
    }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.title("🌱 ZeroWasted")
    st.markdown("---")
    st.button("🏠 Dashboard", use_container_width=True)
    st.button("❤️ Active Needs", use_container_width=True)
    st.button("🎁 Share Surplus", use_container_width=True)
    
    st.markdown("### 📊 Your Impact")
    col_a, col_b = st.columns(2)
    col_a.metric("Helped", "12")
    col_b.metric("Shared", "8")

# --- MAIN PAGE ---

# 1. Welcome Banner
st.markdown("""
<div class="hero-banner">
    <h1>Welcome back, Sarah! 👋</h1>
    <p>You've helped 12 people this month. Together, we're building a caring community.</p>
</div>
""", unsafe_allow_html=True)

# 2. Filters (Visual only for now)
c1, c2, c3 = st.columns([1, 4, 1])
with c1:
    st.selectbox("Sort By", ["Most Recent", "Urgent", "Nearby"], label_visibility="collapsed")
with c2:
    st.text_input("Search", placeholder="Search for food, clothes...", label_visibility="collapsed")
with c3:
    st.button("➕ Post Need", use_container_width=True, type="primary")

st.markdown("### 🟢 Active Needs Nearby")

# --- FETCH DATA & DISPLAY GRID ---
# Fetch all active needs from MongoDB
needs = list(listings_col.find({"status": "active"}))

# Create a grid layout (3 columns wide)
cols = st.columns(3)

for index, need in enumerate(needs):
    # Select which column to add this card to
    col = cols[index % 3]
    
    with col:
        # Determine if we show the Urgent badge
        badge_html = f'<span class="badge">Urgent</span>' if need.get('is_urgent') else ''
        
        # RENDER THE CARD (HTML)
        st.markdown(f"""
        <div class="need-card">
            <div class="user-header">
                <div class="user-info">
                    <img src="{need['avatar']}" class="avatar">
                    <div>
                        <div style="font-weight: 600; font-size: 0.95rem;">{need['user_name']}</div>
                        <div style="color: #6b7280; font-size: 0.8rem;">{need['location']} • {need['timestamp']}</div>
                    </div>
                </div>
                {badge_html}
            </div>
            
            <div style="margin-bottom: 1rem;">
                <h4 style="margin: 0 0 0.5rem 0; font-size: 1.1rem;">
                    <i class="fa-solid {need['category_icon']}" style="color: #00b87c; margin-right: 5px;"></i> 
                    {need['title']}
                </h4>
                <p style="color: #4b5563; font-size: 0.9rem; line-height: 1.5; margin: 0;">
                    {need['description']}
                </p>
            </div>
            
            <div style="border-top: 1px solid #f3f4f6; padding-top: 10px; display: flex; justify-content: space-between; align-items: center;">
                <span class="verified"><i class="fa-solid fa-circle-check"></i> Verified</span>
                <span style="font-size: 0.85rem; color: #6b7280;">❤️ {need['supporters']} supporters</span>
            </div>
        </div>
        """, unsafe_allow_html=True)