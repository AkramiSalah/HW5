class InvalidIdException(Exception):
    pass

class Entry:
    def __init__(self, val, val_name):
        self.val_name = val_name
        self.val = self.validated_val(val)

    def __repr__(self):
        return f"{self.val_name}={self.val}"

class UnsignedIntField(Entry):
    def validated_val(self, val):
        if val < 0 or type(val) is not int:
            raise InvalidIdException(f'{self.val_name} has to be non negative integer!!!')
        return val

    def __int__(self):
        return self.val

    def __eq__(self, rhs):
        isValidArgument = type(rhs) is int or type(rhs) is type(self) 
        return isValidArgument and  int(rhs) == int(self)

class StringField(Entry):
    def validated_val(self, val):
        if type(val) is not str:
            raise InvalidIdException(f'{self.val_name} has to be a string!!!')
        return val
    
    def __repr__(self):
        #override
        return f"{self.val_name}='{self.val}'"


def Field(val, val_name):
    if type(val) is str:
        return StringField(val, val_name)
    elif type(val) is int:
        return UnsignedIntField(val, val_name)
    return Entry(val, val_name)

    
class Customer:
    def __init__(self, id, name, city, address):
        self.id = Field(id, "id")
        self.name = Field(name, "name")
        self.city = Field(city, "city")
        self.address = Field(address, "address")
    
    def __repr__(self):
        return f"{type(self)}({self.id}, {self.name}, {self.city}, {self.address})"

class Supplier(Customer):
    pass


class Product:
    def __init__(self, id, name, price, supplier_id, quantity):
        self.name = name
        self.id = Field(id, "id")
        self.price = Field(price, "price")
        self.supplier_id = Field(supplier_id, "supplier_id")
        self.quantity = Field(quantity, "quantity")

class Order:
    def __init__(self, id, customer_id, product_id, quantity, total_price):
        self.id = Field(id, "id")   
        self.customer_id = Field(customer_id, "customer_id")   
        self.product_id = Field(product_id, "product_id")   
        self.quantity = Field(quantity, "quantity")   
        self.total_price = Field(total_price, "total_price")   