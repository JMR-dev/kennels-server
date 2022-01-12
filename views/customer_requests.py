CUSTOMERS = [
    {
      "id": 1,
      "name": "Ryan Tanay",
      "email": "ryan@tanay.com",
      "employee": false
    },
    {
      "id": 2,
      "name": "Emma Beaton",
      "email": "emma@beaton.com",
      "employee": false
    },
    {
      "id": 3,
      "name": "Dani Adkins",
      "email": "dani.adkins.com",
      "employee": false
    },
    {
      "id": 4,
      "name": "Adam Oswalt",
      "email": "adam@oswalt.com",
      "employee": false
    },
    {
      "id": 5,
      "name": "Fletcher Bangs",
      "email": "flangs@bangs.com",
      "employee": false
    },
    {
      "id": 6,
      "name": "Angela Lee",
      "email": "lee@lee.com",
      "employee": false
    },
    {
      "name": "mike mike",
      "email": "m@m.com",
      "employee": false,
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
