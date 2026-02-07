'''
Inputs:
- time_to_expiry_hours (float)
- distance_km (float)
- match_percentage (float between 0 and 1)

Output:
- urgency_factor (float between 0 and 1)
'''

def calculate_urgency_factor(
    time_to_expiry_hours,
    distance_km,
    match_percentage
):
    # ---------------------------
    # Input sanitization
    # ---------------------------
    time_to_expiry_hours = max(0.0, time_to_expiry_hours)
    distance_km = max(0.0, distance_km)
    match_percentage = max(0.0, min(match_percentage, 1.0))

    # ---------------------------
    # Hard safety rule (optional but recommended)
    # If match is too poor, reject outright
    # ---------------------------
    MIN_MATCH_THRESHOLD = 0.3
    if match_percentage < MIN_MATCH_THRESHOLD:
        return 0.0

    # ---------------------------
    # Expiry urgency component (dominant)
    # Less time → higher urgency
    # ---------------------------
    expiry_urgency = 1 / (time_to_expiry_hours + 1)

    # ---------------------------
    # Distance urgency component (secondary)
    # Shorter distance → higher urgency
    # ---------------------------
    distance_urgency = 1 / (distance_km + 1)

    # ---------------------------
    # Weighted time–distance urgency
    # ---------------------------
    TIME_WEIGHT = 0.7
    DISTANCE_WEIGHT = 0.3

    base_urgency = (
        TIME_WEIGHT * expiry_urgency +
        DISTANCE_WEIGHT * distance_urgency
    )

    # ---------------------------
    # Match gating (CRITICAL FIX)
    # Match scales urgency instead of adding to it
    # ---------------------------
    urgency_factor = match_percentage * base_urgency

    # ---------------------------
    # Clamp final value to [0, 1]
    # ---------------------------
    urgency_factor = max(0.0, min(urgency_factor, 1.0))

    return urgency_factor
