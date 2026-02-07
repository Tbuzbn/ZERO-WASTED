from pymongo import MongoClient

MONGO_URI = ""

client = MongoClient(MONGO_URI)

db = client["zero_wasted"]

listings_col = db["listings"]
requests_col = db["requests"]


# Insertion functions
def add_listing(data: dict):
    """
    Insert a listing document into MongoDB.
    """
    return listings_col.insert_one(data)

def add_request(data: dict):
    """
    Insert a request document into MongoDB.
    """
    return requests_col.insert_one(data)


# Retrieval functions
def get_total_listings() -> int:
    return listings_col.count_documents({})

def get_total_requests() -> int:
    return requests_col.count_documents({})

def get_latest_listings(limit: int = 3):
    return list(
        listings_col.find().sort("_id", -1).limit(limit)
    )

# Delete functions
def delete_listing(listing_id: str):
    """
    Remove a listing after it has been matched.
    """
    return listings_col.delete_one(
        {"_id": ObjectId(listing_id)}
    )

def delete_request(request_id: str):
    """
    Remove a request after it has been matched.
    """
    return requests_col.delete_one(
        {"_id": ObjectId(request_id)}
    )

def complete_match(listing_id: str, request_id: str):
    """
    Complete a match by removing both listing and request.
    """
    delete_listing(listing_id)
    delete_request(request_id)