from types import ID, Price, String, Quantity, Name, Address, CustomerID, ProductID

class Customer:
    def __init__(self, id, name, city, address):
        self.id = ID(id)
        self.name = Name(name)
        self.city = City(city)
        self.address = Address(address)
    
    def __repr__(self):
        return f"{type(self)}({self.id}, {self.name}, {self.city}, {self.address})"

class Supplier(Customer):
    pass

class Product:
    def __init__(self, id, name, price, supplier_id, quantity):
        self.name = Name(name)
        self.id = ID(id)
        self.price = Price(price)
        self.supplier_id = SupplierID(supplier_id)
        self.quantity = Quantity(quantity)

    def __repr__(self):
        return f"{type(self)}({self.id}, {self.name}, {self.price}, {self.supplier_id}, {self.quantity})"

class Order:
    def __init__(self, id, customer_id, product_id, quantity, total_price):
        self.id = ID(id)   
        self.customer_id = ID(customer_id)   
        self.product_id = ID(product_id)   
        self.quantity = Quantity(quantity)   
        self.total_price = Price(total_price)
    
    def __repr__(self):
        return f"{type(self)}({self.id}, {self.customer_id}, {self.product_id}, {self.quantity}, {self.total_price})"
