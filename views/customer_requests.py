CUSTOMERS = [
    {
        "id": 1,
        "name": "Sydney Noh",
        "address": "976 Software School Rd.",
        "email": "sydnoh@gmail.com"
    },
    {
        "id": 2,
        "name": "Trevor Guinn",
        "address": "123 NSS Ln",
        "email": "trevguinn@gmail.com"
    },
    {
        "id": 3,
        "name": "Madi",
        "address": "1420 porter rd",
        "email": "madihepner@gmail.com"
    },
    {
        "id": 4,
        "name": "Bobby Brown",
        "address": "1234 testing rd",
        "email": "bobbybrown@gmail.com"
    },
    {
        "email": "Thepner@aol.com",
        "name": "Tracy Hepner",
        "address": "912 Lewisburg Pike",
        "id": 5
    },
    {
        "id": 6,
        "name": "Jayden Hepner",
        "address": "1420 porter road",
        "email": "jaybae@gmail.com"
    }
]


def get_all_customers():
    return CUSTOMERS

# Function with a single parameter


def get_single_customer(id):
    # Variable to hold the found animal, if it exists
    requested_customer = None

    # Iterate the ANIMALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for customer in CUSTOMERS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer
