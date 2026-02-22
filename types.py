class InvalidIdException(Exception):
    pass
class InvalidPriceException(Exception):
    pass

class Field:
    #this is an abstract calss!!!! there should never actually be a Field obj thats just a Field only through polymorphism
    def validated_val(self, val, expected_type):
        return val
    def __init__(self, val, val_name):
        self.val_name = val_name
        self.val = self.validated_val(val, None)

    def __repr__(self):
        return f"{self.val_name}={self.val}"

class UnsignedField(Field):
    def validated_val(self, val, T):
        if val < 0 or type(val) is not type(T) :
            raise InvalidPriceException(f'{self.val_name} has to be non negative value of type {T}!!!')
        return val

class UnsignedIntField(UnsignedField):
    def validated_val(self, val, T):
        return super().validated_val(val, int)

    def __int__(self):
        return self.val

    def __eq__(self, rhs):
        isValidArgument = type(rhs) is int or type(rhs) is type(self) 
        return isValidArgument and int(rhs) == int(self)


class UnsignedFloatField(UnsignedField):
    def validated_val(self, val, T):
        return super().validated_val(val, type(int))

class StringField(Field):
    def validated_val(self, val):
        if type(val) is not str:
            raise Exception(f'{self.val_name} has to be a string!!!')
        return val
    
    def __repr__(self):
        #override
        return f"{self.val_name}='{self.val}'"
