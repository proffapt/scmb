from database import db
from typing import TypedDict


class ShipmentMetadata(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
    shipment = db.Column(db.String(50), db.ForeignKey(
        'shipment.code'), nullable=False)
    latitude = db.Column(db.String(50))
    longitude = db.Column(db.String(50))
    temperature = db.Column(db.String(50))
    quality = db.Column(db.BigInteger)


class ShipmentMetadataType(TypedDict):
    id: int
    timestamp: str
    shipment: str
    latitude: str
    longitude: str
    temperature: str
    quality: int


def serialize(metadata: ShipmentMetadata) -> ShipmentMetadataType:
    return {
        "id": metadata.id,
        "timestamp": metadata.timestamp.isoformat(),
        "shipment": metadata.shipment,
        "latitude": metadata.latitude,
        "longitude": metadata.longitude,
        "temperature": metadata.temperature,
        "quality": metadata.quality
    }
