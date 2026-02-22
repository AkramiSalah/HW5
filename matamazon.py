class InvalidIdException(Exception):
    pass


class UnsignedIntField:
    def validated_val(self, val):
        if val < 0 or type(val) is not int:
            raise InvalidIdException(f'{self.val_name} has to be non negative integer!!!')
        return val
    
    def __init__(self, val, val_name):
        self.val_name = val_name
        self.val = self.validated_val(val)

    def __repr__(self):
        return f"{self.val_name}={self.val}"
    
    def __int__(self):
        return self.val

    def __eq__(self, rhs):
        isValidArgument = type(rhs) is int or type(rhs) is type(self) 
        return isValidArgument and  int(rhs) == int(self)

class StringField:
    def validated_val(self, val):
        if type(val) is not str:
            raise InvalidIdException(f'{self.val_name} has to be a string!!!')
        return val

    def __init__(self, val, val_name):
        self.val_name = val_name
        self.val = self.validated_val(val)
    
    def __repr__(self):
        return f"{self.val_name}='{self.val}'"


    
class Customer:
    def __init__(self, id, name, city, address):
        self.id = UnsignedIntField(id, "id")
        self.name = StringField(name, "name")
        self.city = StringField(city, "city")
        self.address = StringField(address, "address")
    
    def __repr__(self):
        return f"Customer({self.id}, {self.name}, {self.city}, {self.address})"

class Supplier(Customer):
    pass
    #def __init__(self, id, name, city, address):


class Product:
    def __init__(self, id, name, price, supplier_id, quantity):
        self.name = name
        self.id = UnsignedIntField(id, "id")
        self.price = UnsignedIntField(price, "price")
        self.supplier_id = UnsignedIntField(supplier_id, "supplier_id")
        self.quantity = UnsignedIntField(quantity, "quantity")

class Order:
    def __init__(self, id, customer_id, product_id, quantity, total_price):
        self.id = UnsignedIntField(id, "id")   
        self.customer_id = UnsignedIntField(customer_id, "customer_id")   
        self.product_id = UnsignedIntField(product_id, "product_id")   
        self.quantity = UnsignedIntField(quantity, "quantity")   
        self.total_price = UnsignedIntField(total_price, "total_price")   