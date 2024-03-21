from database import db
from typing import TypedDict


class Person(db.Model):
    username = db.Column(db.String(50), primary_key=True, nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100))
    address = db.Column(db.String(200), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    organisation = db.Column(db.String(100), nullable=False)


class PersonType(TypedDict):
    username: str
    email: str
    password: str
    first_name: str
    last_name: str
    address: str
    phone: str
    organisation: str


def serialize(person: Person) -> PersonType:
    return {
        "username": person.username,
        "email": person.email,
        "password": person.password,
        "first_name": person.first_name,
        "last_name": person.last_name,
        "address": person.address,
        "phone": person.phone,
        "organisation": person.organisation
    }
