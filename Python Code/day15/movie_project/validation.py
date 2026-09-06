def validate_name(name):

    if name.strip() == "":
        raise ValueError("Movie name cannot be empty")

def validate_price(price):

    if price <= 0:
        raise ValueError("Price must be greater than 0")

def validate_seat(seats):

    if seats <= 0:
        raise ValueError("Seats must be greater than 0")

