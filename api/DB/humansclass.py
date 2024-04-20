class Human:
    id: int
    name: str
    surname: str
    patronymic: str
    phone_number: str


class User(Human):
    login: str
    password: str


class Profession(Human):
    license_id: str
    company_name: str

