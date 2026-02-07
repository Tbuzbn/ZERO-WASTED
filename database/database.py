from pymongo import MongoClient

MONGO_URI = "mongodb+srv://zerowasted_rahul:ykBbyBjqaRMBy9tP@zerowastedcluster.5fmxgot.mongodb.net/"

client = MongoClient(MONGO_URI)

db = client["zero_wasted"]

listings_col = db["listings"]
requests_col = db["requests"]


# Insertion functions
def add_listing(data: dict):
    return listings_col.insert_one(data)

def add_request(data: dict):
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
    return listings_col.delete_one(
        {"_id": ObjectId(listing_id)}
    )

def delete_request(request_id: str):
    return requests_col.delete_one(
        {"_id": ObjectId(request_id)}
    )

def complete_match(listing_id: str, request_id: str):
    delete_listing(listing_id)
    delete_request(request_id)