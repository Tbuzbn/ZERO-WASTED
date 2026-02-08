from logic.matching import match_request_to_listings

request = {
    "type": "Food",
    "quantity": 2,
    "location": {"lat": 28.6139, "lng": 77.2090},
    "status": "active"
}

listings = [
    {
        "type": "Food",
        "quantity": 5,
        "location": {"lat": 28.6145, "lng": 77.2100},
        "status": "active"
    },
    {
        "type": "Food",
        "quantity": 1,
        "location": {"lat": 28.6140, "lng": 77.2080},
        "status": "active"
    },
    {
        "type": "Books",
        "quantity": 10,
        "location": {"lat": 28.6200, "lng": 77.2200},
        "status": "active"
    }
]

matches = match_request_to_listings(request, listings)

for m in matches:
    print(m["distance_km"], "km", m["listing"])
