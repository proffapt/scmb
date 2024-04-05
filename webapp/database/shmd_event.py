from . import db
from typing import List
from datetime import datetime
from models.error import DB_Error
from models.shmd_event import SensorHealthMonitoringDeviceEvent, SensorHealthMonitoringDeviceEventType


def get_all_events() -> List[SensorHealthMonitoringDeviceEvent] | DB_Error:
    try:
        sensor_device_events: List[SensorHealthMonitoringDeviceEvent] = SensorHealthMonitoringDeviceEvent.query.all(
        )
        return sensor_device_events
    except Exception as e:
        return {"db_error": str(e)}


def get_all_events_by_sensor_code(sensor_device_code: str) -> List[SensorHealthMonitoringDeviceEvent] | DB_Error:
    try:
        sensor_device_events: List[SensorHealthMonitoringDeviceEvent] = SensorHealthMonitoringDeviceEvent.query.filter_by(
            sensor_health_monitoring_device=sensor_device_code).all()
        return sensor_device_events
    except Exception as e:
        return {"db_error": str(e)}


def get_event(id: int) -> SensorHealthMonitoringDeviceEvent | DB_Error:
    try:
        sensor_device_event = SensorHealthMonitoringDeviceEvent.query.filter_by(
            id=id).first()
        if isinstance(sensor_device_event, SensorHealthMonitoringDeviceEvent):
            return sensor_device_event
        else:
            return {"db_error": "Sensor device event not found"}
    except Exception as e:
        return {"db_error": str(e)}


def create_event(sensor_device_event_details: SensorHealthMonitoringDeviceEventType) -> SensorHealthMonitoringDeviceEvent | DB_Error:
    try:
        sensor_device_event = SensorHealthMonitoringDeviceEvent(
            timestamp=datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
            sensor_health_monitoring_device=sensor_device_event_details.get(
                "sensor_health_monitoring_device"),
            remarks=sensor_device_event_details.get("remarks")
        )
        db.session.add(sensor_device_event)
        db.session.commit()
        return sensor_device_event
    except Exception as e:
        return {"db_error": str(e)}


def update_event(sensor_device_event_details: SensorHealthMonitoringDeviceEventType) -> SensorHealthMonitoringDeviceEvent | DB_Error:
    try:
        event_id = sensor_device_event_details.get("id")
        sensor_device_event: SensorHealthMonitoringDeviceEvent | DB_Error = get_event(
            event_id)
        if isinstance(sensor_device_event, SensorHealthMonitoringDeviceEvent):
            sensor_device_event.timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
            sensor_device_event.sensor_health_monitoring_device = sensor_device_event_details.get(
                "sensor_health_monitoring_device")
            sensor_device_event.remarks = sensor_device_event_details.get(
                "remarks")
            db.session.commit()
            return sensor_device_event
        else:
            return sensor_device_event
    except Exception as e:
        return {"db_error": str(e)}


def delete_event(id: int) -> SensorHealthMonitoringDeviceEvent | DB_Error:
    try:
        sensor_device_event: SensorHealthMonitoringDeviceEvent | DB_Error = get_event(
            id)
        if isinstance(sensor_device_event, SensorHealthMonitoringDeviceEvent):
            db.session.delete(sensor_device_event)
            db.session.commit()
            return sensor_device_event
        else:
            return sensor_device_event
    except Exception as e:
        return {"db_error": str(e)}
