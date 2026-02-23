class InvalidIdException(Exception):
    pass
class InvalidPriceException(Exception):
    pass

class Field:
    #this is an abstract calss!!!! there should never actually be a Field obj thats just a Field only through polymorphism
    def error(self):
        if self.exception:
            raise self.exception(self.exception_message)
        raise Exception("generic Exception")

    def validated_val(self, val):
        if type(val) is not self.type_T:
            self.error()
        return val

    def __init__(self, val, val_name, type_T, exception = None, exception_message = None):
        self.val_name = val_name
        self.type_T = type_T
        self.exception = exception 
        self.exception_message = exception_message
        self.val = self.validated_val(val)

    def __repr__(self):
        return f"{self.val_name}={self.val}"

class UnsignedField(Field):
    def validated_val(self, val):
        val = super().validated_val(val)
        if val < 0:
            self.error()
        return val

class UnsignedIntField(UnsignedField):
    def __init__(self, val, val_name, exception = None, exception_message = None ):
        super().__init__(val, val_name, int, exception, exception_message)
    
    def __int__(self):
        return self.val

    def __eq__(self, rhs):
        isValidArgument = type(rhs) is int or type(rhs) is type(self) 
        return isValidArgument and  int(rhs) == int(self)


class UnsignedFloatField(UnsignedField):
    def __init__(self, val, val_name, exception = None, exception_message = None):
        super().__init__(val, val_name, float, exception, exception_message)


class StringField(Field):
    def validated_val(self, val):
        return super().validated_val(val)
    
    def __init__(self, val, val_name):
        super().__init__(
            val, val_name, str
        )# we assume StringFields are always valid!

    def __repr__(self):
        #override
        return f"{self.val_name}='{self.val}'"


class ID(UnsignedIntField):
    def __init__(self, val, val_name = "id"):
        super().__init__(
            val,
            val_name,
            InvalidIdException,
            f'{val_name} has to be a non-negative integer!!!'
        )
    

class CustomerID(ID):
    def __init__(self, val):
        super().__init__(val, val_name="customer_id")

class ProductID(ID):
    def __init__(self, val):
        super().__init__(val, val_name="product_id")

class SupplierID(ID):
    def __init__(self, val):
        super().__init__(val, val_name="supplier_id")

class Price(UnsignedFloatField):
    def __init__(self, val, val_name = "price"):
        super().__init__(
            val,
            val_name,
            exception = InvalidPriceException,
            exception_message = f'{val_name} has to be a non-negative number!!!'
        )

class Quantity(UnsignedIntField):
    def __init__(self, val, val_name = "quantity"):
        super().__init__(
            val,
            val_name,
            exception = ValueError,
            exception_message=f"{val_name} has to be a non-negative Integer!!!"
        )

class Name(StringField):
    def __init__(self, val):
            super().__init__(
                val,
                val_name = "name",
        )

class City(StringField):
    def __init__(self, val):
            super().__init__(
                val,
                val_name = "city",
        )

class Address(StringField):
    def __init__(self, val):
            super().__init__(
                val,
                val_name = "address",
        )


