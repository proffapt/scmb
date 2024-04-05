from database import db
from typing import TypedDict


class SensorHealthMonitoringDevice(db.Model):
    code = db.Column(db.String(50), primary_key=True, nullable=False)
    shipment = db.Column(db.String(50), db.ForeignKey(
        'shipment.code'), nullable=False)
    description = db.Column(db.String(200), nullable=False)


class SensorHealthMonitoringDeviceType(TypedDict):
    code: str
    shipment: str
    description: str


def serialize(device: SensorHealthMonitoringDevice) -> SensorHealthMonitoringDeviceType:
    return {
        "code": device.code,
        "shipment": device.shipment,
        "description": device.description
    }
