from types import *

class Customer:
    def __init__(self, id, name, city, address):
        self.id = UnsignedIntField(id, "id")
        self.name = StringField(name, "name")
        self.city = StringField(city, "city")
        self.address = StringField(address, "address")
    
    def __repr__(self):
        return f"{type(self)}({self.id}, {self.name}, {self.city}, {self.address})"

class Supplier(Customer):
    pass


class Product:
    def __init__(self, id, name, price, supplier_id, quantity):
        self.name = StringField(name, "name")
        self.id = UnsignedIntField(id, "id")
        self.price = UnsignedFloatField(price, "price")
        self.supplier_id = UnsignedIntField(supplier_id, "supplier_id")
        self.quantity = UnsignedFloatField(quantity, "quantity")

    def __repr__(self):
        return f"{type(self)}({self.id}, {self.name}, {self.price}, {self.supplier_id}, {self.quantity})"

class Order:
    def __init__(self, id, customer_id, product_id, quantity, total_price):
        self.id = UnsignedIntField(id, "id")   
        self.customer_id = UnsignedIntField(customer_id, "customer_id")   
        self.product_id = UnsignedIntField(product_id, "product_id")   
        self.quantity = UnsignedFloatField(quantity, "quantity")   
        self.total_price = UnsignedFloatField(total_price, "total_price")   