from pymongo import MongoClient
from bson import ObjectId

MONGO_URI = "mongodb+srv://zerowasted_rahul:ykBbyBjqaRMBy9tP@zerowastedcluster.5fmxgot.mongodb.net/"

client = MongoClient(MONGO_URI)

db = client["zero_wasted"]

listings_col = db["listings"]
requests_col = db["requests"]


# Insertion functions
def update_listing(listing_id, updates: dict):
    return listings_col.update_one(
        {"_id": ObjectId(listing_id)},
        {"$set": updates}
    )

def add_listing(data: dict):
    return listings_col.insert_one(data)

def add_request(data: dict):
    return requests_col.insert_one(data)

# Retrieval functions
def get_active_listings():
    return list(
        listings_col
        .find({"status": "active"})
        .sort("created_at", -1)
    )
    
def get_active_requests():
    return list(requests_col.find({"status": "active"}))

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