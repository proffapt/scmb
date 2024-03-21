from database import db
from typing import TypedDict


class Shipment(db.Model):
    code = db.Column(db.String(50), primary_key=True, nullable=False)
    supplychain = db.Column(db.BigInteger, db.ForeignKey(
        'supplychain.id'), nullable=False)
    product = db.Column(db.String(50), db.ForeignKey(
        'product.code'), nullable=False)
    quantity = db.Column(db.Float, nullable=False)
    quantity_unit = db.Column(db.String(50), nullable=False)
    acceptable_quality_lower_bound = db.Column(db.BigInteger)
    acceptable_quality_upper_bound = db.Column(db.BigInteger)
    expected_quality = db.Column(db.BigInteger)


class ShipmentType(TypedDict):
    code: str
    supplychain: int
    product: str
    quantity: float
    quantity_unit: str
    acceptable_quality_lower_bound: int
    acceptable_quality_upper_bound: int
    expected_quality: int


def serialize(shipment: Shipment) -> ShipmentType:
    return {
        "code": shipment.code,
        "supplychain": shipment.supplychain,
        "product": shipment.product,
        "quantity": shipment.quantity,
        "quantity_unit": shipment.quantity_unit,
        "acceptable_quality_lower_bound": shipment.acceptable_quality_lower_bound,
        "acceptable_quality_upper_bound": shipment.acceptable_quality_upper_bound,
        "expected_quality": shipment.expected_quality
    }
