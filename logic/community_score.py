def calculate_impact_score(
    people_helped,
    food_waste_avoided_kg,
    max_people_helped,
    max_food_waste_avoided_kg
):
    # Safety checks to avoid division errors
    if max_people_helped <= 0 or max_food_waste_avoided_kg <= 0:
        return 0.0

    # Normalization
    normalized_people = people_helped / max_people_helped
    normalized_waste = food_waste_avoided_kg / max_food_waste_avoided_kg

    # Weights (fixed system parameters)
    PEOPLE_WEIGHT = 0.7
    WASTE_WEIGHT = 0.3

    # Final Impact Score
    impact_score = (
        PEOPLE_WEIGHT * normalized_people +
        WASTE_WEIGHT * normalized_waste
    )

    # Clamp score between 0 and 1
    impact_score = max(0.0, min(impact_score, 1.0))

    return impact_score