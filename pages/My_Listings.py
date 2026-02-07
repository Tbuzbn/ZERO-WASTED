import streamlit as st
from datetime import datetime
from database.database import (
    get_active_listings,
    delete_listing,
    update_listing
)


st.set_page_config(page_title="My Listings | ZERO WASTED", layout="wide")
st.session_state.setdefault("delete_notice", None)


# ---------- STYLE ----------
st.markdown("""
<style>
.card {
  background: #0b1220;
  border-radius: 16px;
  padding: 1.4rem;
  border: 1px solid rgba(255,255,255,0.08);
  margin-bottom: 1rem;
}
.title {
  font-size: 1.8rem;
  font-weight: 800;
  color: #22c55e;
}
.meta {
  font-size: 0.9rem;
  color: #9ca3af;
}
.item-title {
  font-size: 1.1rem;
  font-weight: 700;
}
.item-text {
  font-size: 0.9rem;
  color: #d1d5db;
}
</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown("""
<div class="card">
  <div class="title">My Active Listings</div>
  <div class="meta">Resources you’ve shared with the community</div>
</div>
""", unsafe_allow_html=True)

if st.session_state.get("delete_notice"):
    st.toast("Listing deleted 🗑️", icon="✅")
    st.session_state.delete_notice = None
    
# ---------- FETCH LISTINGS ----------
try:
    listings = get_active_listings()
except Exception as e:
    listings = []
    st.error("Could not fetch listings.")
    st.caption(str(e))

# ---------- EMPTY ----------
if not listings:
    st.info("You have no active listings right now.")
else:
    for item in listings:
        listing_id = str(item["_id"])
        edit_key = f"edit_{listing_id}"

        st.session_state.setdefault(edit_key, False)

        col_main, col_actions = st.columns([5, 2])

        # ---------- CARD ----------
        with col_main:
            st.markdown(f"""
            <div class="card">
              <div class="item-title">
                {item.get("quantity")} × {item.get("type")}
              </div>
              <div class="item-text">
                <strong>Location:</strong> {item.get("location_label", "Not specified")}<br>
                <strong>Message:</strong> {item.get("message", "—")}
              </div>
            </div>
            """, unsafe_allow_html=True)

        # ---------- ACTIONS ----------
        with col_actions:
            if st.button("✏️ Edit", key=f"edit_btn_{listing_id}", use_container_width=True):
                st.session_state[edit_key] = True

            if st.button("🗑️ Delete", key=f"delete_{listing_id}", use_container_width=True):
              try:
                  delete_listing(listing_id)
                  st.session_state.delete_notice = "Listing deleted successfully."
                  st.rerun()
              except Exception as e:
                  st.error("Failed to delete listing.")
                  st.caption(str(e))


        # ---------- EDIT FORM ----------
        if st.session_state.get(edit_key):
            with st.form(f"edit_form_{listing_id}"):
                new_quantity = st.number_input(
                    "Quantity",
                    min_value=1,
                    value=int(item.get("quantity", 1))
                )

                new_message = st.text_area(
                    "Message",
                    value=item.get("message", ""),
                    height=80
                )

                new_location = st.text_input(
                    "Location",
                    value=item.get("location_label", "")
                )

                save = st.form_submit_button("💾 Save Changes")
                cancel = st.form_submit_button("Cancel")

                if save:
                    try:
                        update_listing(
                            listing_id,
                            {
                                "quantity": new_quantity,
                                "message": new_message.strip(),
                                "location_label": new_location.strip(),
                                "updated_at": datetime.utcnow()
                            }
                        )
                        st.success("Listing updated.")
                        st.session_state[edit_key] = False
                        st.rerun()
                    except Exception as e:
                        st.error("Failed to update listing.")
                        st.caption(str(e))

                if cancel:
                    st.session_state[edit_key] = False
                    st.rerun()
