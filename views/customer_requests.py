CUSTOMERS = [
    {
      "id": 1,
      "name": "Ryan Tanay",
      "email": "ryan@tanay.com",
      "employee": False
    },
    {
      "id": 2,
      "name": "Emma Beaton",
      "email": "emma@beaton.com",
      "employee": False
    },
    {
      "id": 3,
      "name": "Dani Adkins",
      "email": "dani.adkins.com",
      "employee": False
    },
    {
      "id": 4,
      "name": "Adam Oswalt",
      "email": "adam@oswalt.com",
      "employee": False
    },
    {
      "id": 5,
      "name": "Fletcher Bangs",
      "email": "flangs@bangs.com",
      "employee": False
    },
    {
      "id": 6,
      "name": "Angela Lee",
      "email": "lee@lee.com",
      "employee": False
    },
    {
      "name": "mike mike",
      "email": "m@m.com",
      "employee": False,
      "id": 7
    },

             ]

def get_all_customers():
    return CUSTOMERS

def get_single_customer():
    requested_customer = None


    for customer in CUSTOMERS:
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer
