import math



def calculate_monthly_community_score(
    food_kg,
    clothes_kg,
    books_count,
    months_ago
):
    """
    Community score rules:
    - No decay for first 2 full months
    - Gradual decay starts after 2 months
    """

    # Sanitize inputs
    food_kg = max(0.0, food_kg)
    clothes_kg = max(0.0, clothes_kg)
    books_count = max(0, books_count)
    months_ago = max(0, months_ago)

    # Conversion constants
    FOOD_PER_PERSON = 0.5
    CLOTHES_PER_PERSON = 2.0

    # Resource weights (sum = 1)
    FOOD_WEIGHT = 0.5
    CLOTHES_WEIGHT = 0.3
    BOOKS_WEIGHT = 0.2

    # Convert to impact units
    food_impact = food_kg / FOOD_PER_PERSON
    clothes_impact = clothes_kg / CLOTHES_PER_PERSON
    books_impact = books_count

    # Square-root growth (anti-gaming)
    food_impact = math.sqrt(food_impact)
    clothes_impact = math.sqrt(clothes_impact)
    books_impact = math.sqrt(books_impact)

    # Raw monthly score
    raw_score = (
        FOOD_WEIGHT * food_impact +
        CLOTHES_WEIGHT * clothes_impact +
        BOOKS_WEIGHT * books_impact
    )

    # ---- Time decay (starts AFTER 2 months) ----
    DECAY_RATE = 0.15
    effective_months = max(0, months_ago - 2)
    decay_factor = math.exp(-DECAY_RATE * effective_months)

    return raw_score * decay_factor



def calculate_total_community_score(monthly_data):
    """
    monthly_data: list of dicts
    Each dict:
    {
        "food": kg,
        "clothes": kg,
        "books": count,
        "months_ago": int
    }
    """

    total_score = 0.0

    for month in monthly_data:
        total_score += calculate_monthly_community_score(
            food_kg=month["food"],
            clothes_kg=month["clothes"],
            books_count=month["books"],
            months_ago=month["months_ago"]
        )

    return total_score