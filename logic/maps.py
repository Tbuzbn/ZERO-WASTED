# import streamlit as st
# from streamlit_geolocation import streamlit_geolocation
import requests

# st.title("User Location App")

# # Get location data
# location1 = streamlit_geolocation()
# location2 = streamlit_geolocation()

# FIXED_LOCATION1 = {
#     "latitude": 28.6139,
#     "longitude": 77.2090,
#     "accuracy": 0,
#     "altitude": None,
#     "speed": None,
#     "heading": None
# }


# Process and display the location
# if location:
#     if location.get('latitude') is not None and location.get('longitude') is not None:
#         st.success("Location retrieved!")
#         st.write(f"Latitude: {location['latitude']}")
#         st.write(f"Longitude: {location['longitude']}")

#         # Display location on a map
#         st.warning("Location information is not available. Please ensure location permissions are granted.")
# else:
#     st.info("Waiting for location data...")



location1 = FIXED_LOCATION1 = {
    "latitude": 28.6139,
    "longitude": 77.2090,
    "accuracy": 0,
    "altitude": None,
    "speed": None,
    "heading": None
}

location2 = FIXED_LOCATION2 = {
    "latitude": 29.6239,
    "longitude": 77.2090,
    "accuracy": 0,
    "altitude": None,
    "speed": None,
    "heading": None
}


def distance(location1, location2):
    lat1 = location1["latitude"]
    lon1 = location1["longitude"]

    lat2 = location2["latitude"]
    lon2 = location2["longitude"]

    url = (
        f"http://router.project-osrm.org/route/v1/driving/"
        f"{lon1},{lat1};{lon2},{lat2}"
        "?overview=false"
    )

    res = requests.get(url).json()

    if "routes" not in res or not res["routes"]:
        return -1

    distance_m = res["routes"][0]["distance"]
    return int(distance_m / 1000)



print(distance(location1, location2))