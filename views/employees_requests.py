EMPLOYEES = [
    {
      "id": 1,
      "name": "Jessica Younker",
      "email": "jessica@younker.com",
      "employee": True
    },
    {
      "id": 2,
      "name": "Jordan Nelson",
      "email": "jordan@nelson.com",
      "employee": True
    },
    {
      "id": 3,
      "name": "Zoe LeBlanc",
      "email": "zoe@leblanc.com",
      "employee": True
    },
    {
      "name": "Meg Ducharme",
      "email": "meg@ducharme.com",
      "id": 4,
      "employee": True
    },
    {
      "name": "Hannah Hall",
      "email": "hannah@hall.com",
      "id": 5,
      "employee": True
    },
    {
      "name": "Emily Lemmon",
      "email": "emily@lemmon.com",
      "id": 6,
      "employee": True
    },
    {
      "name": "Jordan Castelloe",
      "email": "jordan@castelloe.com",
      "id": 7,
      "employee": True
    },
    {
      "name": "Leah Gwin",
      "email": "leah@gwin.com",
      "id": 8,
      "employee": True
    },
    {
      "name": "Caitlin Stein",
      "email": "caitlin@stein.com",
      "id": 9,
      "employee": True
    },
    {
      "name": "Greg Korte",
      "email": "greg@korte.com",
      "id": 10,
      "employee": True
    },
    {
      "name": "Charisse Lambert",
      "email": "charisse@lambert.com",
      "id": 11,
      "employee": True
    },
    {
      "name": "Madi Peper",
      "email": "madi@peper.com",
      "id": 12,
      "employee": True
    },
    {
      "name": "Jenna Solis",
      "email": "jenna@solis.com",
      "id": 14,
      "employee": True
    },

]

def get_all_employees():
    return EMPLOYEES

def get_single_employee():
    requested_employee = None


    for employee in EMPLOYEES:
        if EMPLOYEES["id"] == id:
            requested_EMPLOYEE = employee

    return requested_employee

def create_employee(employee):
    # Get the id value of the last location in the list
    max_id = EMPLOYEES[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the location dictionary
    employee["id"] = new_id

    # Add the location dictionary to the list
    EMPLOYEES.append(employee)

    # Return the dictionary with `id` property added
    return employee
def delete_employee(id):
    # Initial -1 value for employee index, in case one isn't found
    employee_index = -1

    # Iterate the EMPLOYEES list, but use enumerate() so that you
    # can access the index value of each item
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            # Found the employee. Store the current index.
            employee_index = index

    # If the employee was found, use pop(int) to remove it from list
    if employee_index >= 0:
        EMPLOYEES.pop(employee_index)
