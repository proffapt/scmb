from database import db
from typing import TypedDict


class ShipmentEvent(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
    shipment = db.Column(db.String(50), db.ForeignKey(
        'shipment.code'), nullable=False)
    event = db.Column(db.String(200), nullable=False)


class ShipmentEventType(TypedDict):
    id: int
    timestamp: str
    shipment: str
    event: str


def serialize(event: ShipmentEvent) -> ShipmentEventType:
    return {
        "id": event.id,
        "timestamp": event.timestamp.isoformat(),
        "shipment": event.shipment,
        "event": event.event
    }
