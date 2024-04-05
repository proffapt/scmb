
from database import db
from typing import TypedDict


class SensorHealthMonitoringDeviceEvent(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, nullable=False)
    sensor_health_monitoring_device = db.Column(db.String(50), db.ForeignKey(
        'sensor_health_monitoring_device.code'), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
    remarks = db.Column(db.String(200), nullable=False)


class SensorHealthMonitoringDeviceEventType(TypedDict):
    id: int
    sensor_health_monitoring_device: str
    timestamp: str
    remarks: str


def serialize(event: SensorHealthMonitoringDeviceEvent) -> SensorHealthMonitoringDeviceEventType:
    return {
        "id": event.id,
        "sensor_health_monitoring_device": event.sensor_health_monitoring_device,
        "timestamp": event.timestamp.isoformat(),
        "remarks": event.remarks
    }
