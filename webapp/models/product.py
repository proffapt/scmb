from database import db
from typing import TypedDict


class Product(db.Model):
    code = db.Column(db.String(50), primary_key=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)


class ProductType(TypedDict):
    code: str
    name: str


def serialize(product: Product) -> ProductType:
    return {
        "code": product.code,
        "name": product.name
    }
