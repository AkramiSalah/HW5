class InvalidIdException(Exception):
    pass


class NonNegativeVal:
    def validated_val(self, val):
        if val < 0:
            raise InvalidIdException(f'{self.val_name} has to be non negative!')
        return val
    
    def __init__(self, val, val_name):
        self.val_name = val_name
        self.val = self.validated_val(val)

    def __repr__(self):
        return str(self.val)
    
    def __int__(self):
        return val

    def __eq__(self, rhs):
        return self.val == rhs.val

    
class Customer:
    def __init__(self, id, name, city, address):
        self.id = NonNegativeVal(id, "id")
        self.name = name
        self.city = city
        self.address = address

class Supplier(Customer):
    pass
    #def __init__(self, id, name, city, address):


class Product:
    def __init__(self, id, name, price, supplier_id,  quantity):
        self.name = name
        self.id = NonNegativeVal(id, "id")
        self.price = NonNegativeVal(price, "price")
        self.supplier_id = NonNegativeVal(supplier_id, "supplier_id")
        self.quantity = NonNegativeVal(quantity, "quantity")