class InvalidIdException(Exception):
    pass


class UnsignedInt:
    def validated_val(self, val):
        if val < 0 or type(val) is not int:
            raise InvalidIdException(f'{self.val_name} has to be non negative integer!!!')
        return val
    
    def __init__(self, val, val_name):
        self.val_name = val_name
        self.val = self.validated_val(val)

    def __repr__(self):
        return str(self.val)
    
    def __int__(self):
        return int(self.val)

    def __eq__(self, rhs):
        return int(rhs) == int(self)

    
class Customer:
    def __init__(self, id, name, city, address):
        self.id = UnsignedInt(id, "id")
        self.name = name
        self.city = city
        self.address = address

class Supplier(Customer):
    pass
    #def __init__(self, id, name, city, address):


class Product:
    def __init__(self, id, name, price, supplier_id,  quantity):
        self.name = name
        self.id = UnsignedInt(id, "id")
        self.price = UnsignedInt(price, "price")
        self.supplier_id = UnsignedInt(supplier_id, "supplier_id")
        self.quantity = UnsignedInt(quantity, "quantity")

class Order:
    def __init__(self, id, customer_id, product_id, quantity, total_price):
        self.id = UnsignedInt(id)   
        self.customer_id = UnsignedInt(customer_id)   
        self.product_id = UnsignedInt(product_id)   
        self.quantity = UnsignedInt(quantity)   
        self.total_price = UnsignedInt(total_price)   