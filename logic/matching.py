import math
import sys
import os
import streamlit as st


def match_request_to_listings(request, listings, max_distance_km=5.0):

    # Safety checks
    if request.get("status") != "active":
        return []

    req_loc = request.get("location")
    if not req_loc:
        return []

    matches = []

    for listing in listings:
        # Rule 1: listing must be active
        if listing.get("status") != "active":
            continue

        # Rule 2: resource type must match
        if listing.get("type") != request.get("type"):
            continue

        # Rule 3: quantity must be sufficient
        if listing.get("quantity", 0) < request.get("quantity", 0):
            continue

        # Rule 4: listing must have a location
        lst_loc = listing.get("location")
        if not lst_loc:
            continue

        # Rule 5: compute distance
        distance = haversine_km(
            req_loc["lat"], req_loc["lng"],
            lst_loc["lat"], lst_loc["lng"]
        )

        if distance > max_distance_km:
            continue

        matches.append({
            "listing": listing,
            "distance_km": round(distance, 2)
        })

    # Rule 6: closest first
    matches.sort(key=lambda x: x["distance_km"])

    return matches



def haversine_km(lat1, lng1, lat2, lng2):
    R = 6371  # Earth radius in km

    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lng2 - lng1)

    a = (
        math.sin(dphi / 2) ** 2
        + math.cos(phi1) * math.cos(phi2)
        * math.sin(dlambda / 2) ** 2
    )

    return 2 * R * math.atan2(math.sqrt(a), math.sqrt(1 - a))