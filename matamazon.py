class InvalidIdException(Exception):
    pass


class IdentifiedEntity:
    def validated_id(self, id):
        if id < 0:
            raise InvalidIdException("id has to be non negative!")
        return id
    
    def __init__(self, id):
        self.id = self.validated_id(id)

    
class Customer(IdentifiedEntity):
    def __init__(self, id, name, city, address):
        super().__init__(id)
        self.name = name
        self.city = city
        self.address = address

class Supplier(Customer):
    pass
    #def __init__(self, id, name, city, address):


class Product:
    def __init__(self, id, name, city, address):