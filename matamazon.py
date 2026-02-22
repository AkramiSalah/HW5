class InvalidIdException(Exception):
    pass


class Customer:
    def validate(self):
        if self.id < 0:
            raise InvalidIdException("id has to be non negative!")
        
    def __init__(self, id, name, city, address):
        self.id = id
        self.name = name
        self.city = city
        self.address = address
        self.validate()

class Supplier(Customer):
    pass
    #def __init__(self, id, name, city, address):


