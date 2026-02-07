import streamlit as st

def detect_location(state_prefix="location"):
    label_key = f"{state_prefix}_label"
    coords_key = f"{state_prefix}_coords"

    st.session_state.setdefault(label_key, "")
    st.session_state.setdefault(coords_key, None)

    if st.button("📍 Detect My Location", key=f"{state_prefix}_detect"):
        # Demo coordinates (replace later with real geolocation)
        coords = {"lat": 28.6139, "lng": 77.2090}

        label = f"Lat: {coords['lat']}, Lng: {coords['lng']}"

        st.session_state[coords_key] = coords
        st.session_state[label_key] = label

        st.success("Location detected successfully.")


def location_display(state_prefix="location"):
    label_key = f"{state_prefix}_label"
    coords_key = f"{state_prefix}_coords"

    label = st.session_state.get(label_key)
    coords = st.session_state.get(coords_key)

    if label:
        st.markdown(f"**📍 Location:** {label}")

    if coords:
        st.caption(f"Latitude: {coords['lat']} | Longitude: {coords['lng']}")


def location_input(state_prefix="location"):
    label_key = f"{state_prefix}_label"

    return st.text_input(
        "Area / Locality",
        placeholder="e.g. Indiranagar, Bengaluru",
        key=label_key
    )