from logic.database import add_listing, get_total_listings

add_listing({
    "resource_type": "Food",
    "quantity": 10,
    "message": "Test insert"
})

print("Total listings:", get_total_listings())
