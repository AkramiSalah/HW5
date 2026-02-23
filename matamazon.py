from types import ID, Price, String, Quantity

class Customer:
    def __init__(self, id, name, city, address):
        self.id = ID(id, "id")
        self.name = String(name, "name")
        self.city = String(city, "city")
        self.address = String(address, "address")
    
    def __repr__(self):
        return f"{type(self)}({self.id}, {self.name}, {self.city}, {self.address})"

class Supplier(Customer):
    pass

class Product:
    def __init__(self, id, name, price, supplier_id, quantity):
        self.name = String(name, "name")
        self.id = ID(id, "id")
        self.price = Price(price)
        self.supplier_id = ID(supplier_id, "supplier_id")
        self.quantity = Quantity(quantity)

    def __repr__(self):
        return f"{type(self)}({self.id}, {self.name}, {self.price}, {self.supplier_id}, {self.quantity})"

class Order:
    def __init__(self, id, customer_id, product_id, quantity, total_price):
        self.id = ID(id, "id")   
        self.customer_id = ID(customer_id, "customer_id")   
        self.product_id = ID(product_id, "product_id")   
        self.quantity = Quantity(quantity)   
        self.total_price = Price(total_price, "total_price")
    
    def __repr__(self):
        return f"{type(self)}({self.id}, {self.customer_id}, {self.product_id}, {self.quantity}, {self.total_price})"
