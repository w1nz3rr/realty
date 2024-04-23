import datetime


class Address:
    area: str
    city: str
    neighborhood: str
    street: str
    house_number: int
    flat_number: int

    def __str__(self):
        return self.__dict__


class Builder:
    builder_id: int
    name_builder: str
    director_builder: str
    phone_number: str

    def __str__(self):
        return self.__dict__


class Contractor:
    contractor_id: int
    name_contractor: str
    director_contractor: str
    phone_number: str

    def __str__(self):
        return self.__dict__


class Passport_object:
    passport_id: int

    def __init__(self):
        self.builder = Builder()
        self.contractor = Contractor()

    start_building: datetime.datetime
    end_building: datetime.datetime


class Object:
    object_id: int
    seller_id: int
    type_object: str

    def __init__(self):
        self.address = Address()
        self.passport = Passport_object()

    square: int
    number_of_rooms: int
