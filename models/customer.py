class Customer():
    '''Factory class for customer objects'''
    def __init__(self, id, name, address, email, password):
        self.id = id
        self.name = name
        self.address = address
        self.email = email
        self.password = password