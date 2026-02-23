from matamazon_types import *

class Customer:
    def __init__(self, id, name, city, address):
        self.id = ID(id)
        self.name = Name(name)
        self.city = City(city)
        self.address = Address(address)
    
    def __repr__(self):
        return f"Customer({self.id}, {self.name}, {self.city}, {self.address})"

class Supplier(Customer):
    def __repr__(self):
        return f"Supplier({self.id}, {self.name}, {self.city}, {self.address})"

class Product:
    def __init__(self, id, name, price, supplier_id, quantity):
        self.id = ID(id)
        self.name = Name(name)
        self.price = Price(price)
        self.supplier_id = SupplierID(supplier_id)
        self.quantity = Quantity(quantity)

    def __repr__(self):
        return f"Product({self.id}, {self.name}, {self.price}, {self.supplier_id}, {self.quantity})"

class Order:
    def __init__(self, id, customer_id, product_id, quantity, total_price):
        self.id = ID(id)   
        self.customer_id = CustomerID(customer_id)   
        self.product_id = ProductID(product_id)   
        self.quantity = Quantity(quantity)   
        self.total_price = Price(total_price)
    
    def __repr__(self):
        return f"Order({self.id}, {self.customer_id}, {self.product_id}, {self.quantity}, {self.total_price})"

class MatamazonSystem:
    def __init__(self):
        self.customers = {} # custumer.id -> customer
        self.suppliers = {} # supplier.id -> supplier 
        self.products = {} # product id -> product
        self.orders = {} # order id -> order
        self.order_id_counter = 1
    
    def register_entity(self, entity, is_customer):
        container = self.suppliers
        if is_customer:
            container = self.customers

        if entity.id in container:
            raise InvalidIdException( type(entity).__name__ + " is already registered!!!")
        container[entity.id] = entity

        
    def add_or_update_product(self, product):
        if product.id in self.products.keys():
            if self.products[product.id].supplier_id == product.supplier_id:
                self.products[product.id] = product
            else:
                raise InvalidIdException("another supplier owns this product_id!!!")
        else:
            self.products[product.id] = product

    def place_order(self, customer_id, product_id, quantity = 1):
        if product_id not in self.products.keys():
            return "The product does not exist in the system"
        if customer_id not in self.customers.keys():
            return "The customer does not exist in the system"

        product = self.products[product_id]

        if product.quantity < quantity:
            return "The quantity requested for this product is greater than the quantity in stock."

        order_price = product.price * quantity
        order = Order(self.order_id_counter, customer_id, product_id, quantity, order_price)
        self.order_id_counter += 1
        product.quantity -= quantity
        self.orders[order.id] = order
    
    def remove_object(self, id, class_type):
        class_type = class_type.strip().lower()
        if class_type == "order":
            return self.remove_order(id)
        
        for order in self.orders.values():
            if self.get_id(order, class_type) == id:
                raise InvalidIdException(
                    f"cannot delete this {class_type} its still in use!!!"
                )
        
        if class_type == "supplier":
            del self.suppliers[id]
        elif class_type == "product":
            del self.products[id]
        elif class_type == "customer":
            del self.customers[id]

    def remove_order(self, id):
        id = ID(id) 
        if id not in self.orders:
            raise InvalidIdException("non existant ordder id!!!")
        order_quantity = self.orders[id].quantity
        self.products[self.orders[id].product_id].quantity += order_quantity
        del self.orders[id]
        return order_quantity


    def get_id(self, order, class_type):
        if class_type == "supplier":
            product = self.products[order.product_id]
            return product.supplier_id
        elif class_type == "product":
            return order.product_id
        elif class_type == "customer":
            return order.customer_id


    

        




