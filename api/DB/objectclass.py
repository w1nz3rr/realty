class Address:
    area: str
    city: str
    neighborhood: str
    street: str
    house_number: int
    flat_number: int

    def __str__(self):
        return self.__dict__


class Object:
    object_id: int
    seller_id: int
    type_object: str

    def __init__(self):
        self.address = Address()

    def print(self):
        obj = self
        obj.address = obj.address.__dict__
        return obj.__dict__

