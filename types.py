class InvalidIdException(Exception):
    pass
class InvalidPriceException(Exception):
    pass

class Field:
    #this is an abstract calss!!!! there should never actually be a Field obj thats just a Field only through polymorphism
    def error(self):
        raise self.exception(self.exception_message)

    def validated_val(self, val):
        if type(val) is not self.type_T:
            self.error()
        return True
    def __init__(self, val, val_name, type_T, exception, exception_message):
        self.val_name = val_name
        self.val = self.validated_val(val)

    def __repr__(self):
        return f"{self.val_name}={self.val}"

class UnsignedField(Field):
    def validated_val(self, val):
        if super().validated_val(val):
            if val >= 0:
                return val
        self.error()

class UnsignedIntField(UnsignedField):
    def __init__(self, val, val_name, type_T, exception, exception_message):
        super().__init__(val, val_name, int, exception, exception_message)
    
    def __int__(self):
        return self.val

    def __eq__(self, rhs):
        isValidArgument = type(rhs) is int or type(rhs) is type(self) 
        return isValidArgument and  int(rhs) == int(self)


class UnsignedFloatField(UnsignedField):
    def __init__(self, val, val_name, type_T, exception, exception_message):
        super().__init__(val, val_name, float, exception, exception_message)

class StringField(Field):
    # def validated_val(self, val):
    #     if type(val) is not str:
    #         raise InvalidIdException(f'{self.val_name} has to be a string!!!')
    #     return val

    def __repr__(self):
        #override
        return f"{self.val_name}='{self.val}'"

class ID(UnsignedIntField):
    def __init__(self, val, val_name = "id"):
        self.exception = InvalidIdException
        self.exception_message = f'{val_name} has to be a non-negative integer!!!'
        super().__init__(val, val_name, int, self.exception, self.exception_message)

class Price(UnsignedFloatField):
    def 
