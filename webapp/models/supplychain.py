from database import db
from typing import TypedDict


class Supplychain(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(100), nullable=False)


class SupplychainType(TypedDict):
    id: int
    name: str


def serialize(supplychain: Supplychain) -> SupplychainType:
    return {
        "id": supplychain.id,
        "name": supplychain.name,
    }
