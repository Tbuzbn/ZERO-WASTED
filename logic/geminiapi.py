from google import genai
import numpy as np
from typing import List, Dict, Any

# -------------------------------------------------
# CONFIG (move API key to env later if needed)
# -------------------------------------------------
GEMINI_API_KEY = "AIzaSyDaZOYWB6xvN2fAObAhwO2zRWE0oh9FRSM"
EMBEDDING_MODEL = "models/gemini-embedding-001"

# Initialize Gemini client once
_client = genai.Client(api_key=GEMINI_API_KEY)


# -------------------------------------------------
# INTERNAL UTILITIES
# -------------------------------------------------
def _cosine_similarity(v1: np.ndarray, v2: np.ndarray) -> float:
    return float(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)))


def _get_embedding(text: str) -> np.ndarray:
    response = _client.models.embed_content(
        model=EMBEDDING_MODEL,
        contents=text
    )
    return np.array(response.embeddings[0].values, dtype=float)


# -------------------------------------------------
# PUBLIC FEATURE FUNCTION
# -------------------------------------------------
def get_matching_score(
    main_message: str,
    other_messages: List[str],
    threshold: float = 60.0
) -> Dict[str, Any]:
    """
    Compare one message with multiple messages using Gemini embeddings.

    Returns:
    {
        "best_message": str | None,
        "best_score": float,
        "match_found": bool,
        "all_scores": List[Tuple[str, float]]
    }
    """

    if not main_message.strip():
        raise ValueError("main_message cannot be empty")

    if not other_messages:
        raise ValueError("other_messages cannot be empty")

    main_embedding = _get_embedding(main_message)

    best_score = 0.0
    best_message = None

    for message in other_messages:
        if not message.strip():
            continue

        emb = _get_embedding(message)
        score = round(_cosine_similarity(main_embedding, emb) * 100, 2)


        if score > best_score:
            best_score = score
            best_message = message

    return {
        "best_message": best_message,
        "best_score": best_score,
        "match_found": best_score >= threshold,
    }

