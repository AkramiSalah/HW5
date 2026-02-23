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

# class SystemContainer:
#     def __init__(self);
#         self.container = {}

#     def append(self, entity_id, entity):
#         if entity_id is in self.container:
#             return False
#         self.container[entity.id] = entity
#         return True
    
#     def remove(self, entity_id):
#         if entity_id is not in self.container:
#             return False

#         del self.container[entity.id]
#         return True

# class Products(SystemContainer):
#     def append(self, entity_id, entity):
#         append_res = super().append(entity_id, entity)
#         if append_res:
#             return True
#         # now we can assume the append res is false 
#         # so we gotta do additional checks..
#         if self.container[entity.id].supplier == entity.supplier_id:
#                 self.container[entity.id] = entity
#             else:
#                 raise InvalidIdException("another supplier owns this product_id!!!")



class MatamazonSystem:
    def __init__(self):
        self.customers = {} # custumer.id -> customer
        self.suppliers = {} # supplier.id -> supplier 
        self.products = {} # product id -> product
        self.orders = {} # order id -> order
    
    def register_entity(self, entity, is_customer):
        container = suppliers
        if is_customer:
            container = customers

        if entity.id is in container:
            raise InvalidIdException( entity.__name__ + " is already registered!!!")
        container[entity.id] = entity

        
    def add_or_update_product(self, product):
        if product.id in products.keys():
            if products[product.id].supplier == product.supplier_id:
                products[product.id] = product
            else:
                raise InvalidIdException("another supplier owns this product_id!!!")
        else:
            products[product.id] = product

    def place_order(self, customer_id, product_id, quantity = 1):
        if product_id is not in products.keys():
            return "The product does not exist in the system"
        if customer_id is not in customers.keys():
            return "The customer does not exist in the system"

        product = products[product_id]
        customer = customers[customer_id]

        if product.quantity < quantity:
            return "The quantity requested for this product is greater than the quantity in stock."

        order_id_str = str(product_id) + str(customer_id) # i hope this is unique enough..
        order_id = int(order_id_str)
        order_price = product.price * quantity
        order = Order(order_id, customer_id, product_id, quantity, order_price)
        orders[order.id] = order
    
    def remove_object(self, id, class_type):
        class_type = class_type.strip().lower()
        if class_type == "order":
            return self.remove_order(id)
        
        id_pairs_of_entities_related_to_order = [(order.customer_id,]


        self.customers
        self.suppliers 
        self.products 
        self.orders  

    def remove_order(self, id):
        id = ID(id) 
        if id is not in orders:
            raise InvalidIdException("non existant ordder id!!!")
        order_quantity = order.quantity
        del orders[id]
        return order_quantity

    def product_owner(self, supplier_id, product_id):
        for product in products.values():
            if product.id == product_id:
                return product.supplier_id
        return -1  

    

        




