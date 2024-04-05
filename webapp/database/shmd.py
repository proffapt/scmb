from . import db
from typing import List
from models.error import DB_Error
from models.shmd_event import SensorHealthMonitoringDeviceEvent
from models.shmd import SensorHealthMonitoringDevice, SensorHealthMonitoringDeviceType


def get_all_sensor_devices() -> List[SensorHealthMonitoringDevice] | DB_Error:
    try:
        sensor_devices: List[SensorHealthMonitoringDevice] = SensorHealthMonitoringDevice.query.all(
        )
        return sensor_devices
    except Exception as e:
        return {"db_error": str(e)}


def get_all_sensor_device_by_shipment(shipment: str) -> List[SensorHealthMonitoringDevice] | DB_Error:
    try:
        sensor_devices: List[SensorHealthMonitoringDevice] = SensorHealthMonitoringDevice.query.filter_by(shipment=shipment).all(
        )
        return sensor_devices
    except Exception as e:
        return {"db_error": str(e)}


def get_sensor_device(code: str) -> SensorHealthMonitoringDevice | DB_Error:
    try:
        sensor_device = SensorHealthMonitoringDevice.query.filter_by(
            code=code).first()
        if isinstance(sensor_device, SensorHealthMonitoringDevice):
            return sensor_device
        else:
            return {"db_error": "Sensor device not found"}
    except Exception as e:
        return {"db_error": str(e)}


def create_sensor_device(sensor_device_details: SensorHealthMonitoringDeviceType) -> SensorHealthMonitoringDevice | DB_Error:
    try:
        check_sensor_device: SensorHealthMonitoringDevice | DB_Error = get_sensor_device(
            sensor_device_details.get("code"))
        if isinstance(check_sensor_device, SensorHealthMonitoringDevice):
            return {"db_error": "Sensor device already exists"}
        else:
            sensor_device = SensorHealthMonitoringDevice(
                code=sensor_device_details.get("code"),
                shipment=sensor_device_details.get("shipment"),
                description=sensor_device_details.get("description")
            )
            db.session.add(sensor_device)
            db.session.commit()
            return sensor_device
    except Exception as e:
        return {"db_error": str(e)}


def update_sensor_device(sensor_device_details: SensorHealthMonitoringDeviceType) -> SensorHealthMonitoringDevice | DB_Error:
    try:
        sensor_device: SensorHealthMonitoringDevice | DB_Error = get_sensor_device(
            sensor_device_details.get("code"))
        if isinstance(sensor_device, SensorHealthMonitoringDevice):
            sensor_device.shipment = sensor_device_details.get("shipment")
            sensor_device.description = sensor_device_details.get(
                "description")
            db.session.commit()
            return sensor_device
        else:
            return sensor_device
    except Exception as e:
        return {"db_error": str(e)}


def delete_sensor_device(code: str) -> SensorHealthMonitoringDevice | DB_Error:
    try:
        sensor_device: SensorHealthMonitoringDevice | DB_Error = get_sensor_device(
            code)
        if isinstance(sensor_device, SensorHealthMonitoringDevice):
            # Delete the connected entries in Sensor_Health_Monitoring_Device_Event table
            db.session.query(SensorHealthMonitoringDeviceEvent).filter(
                SensorHealthMonitoringDeviceEvent.sensor_health_monitoring_device == code).delete()
            # Delete the shipment entry
            db.session.delete(sensor_device)
            # Commit the changes
            db.session.commit()
            return sensor_device
        else:
            return sensor_device
    except Exception as e:
        return {"db_error": str(e)}
