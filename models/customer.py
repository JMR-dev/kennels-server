class Customer():
    '''Factory class for customer objects'''
    def __init__(self, id, name, email) -> None:
        self.id = id
        self.name = name
        self.email = email