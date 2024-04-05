from models.shmd import *
from database.shmd import *
from models.error import API_Error
from flask import Response, request, jsonify
from middleware.auth import login_authorisation


@login_authorisation
def get(code: str) -> tuple[Response, int] | tuple[API_Error, int]:
    if code.casefold() == "all":
        try:
            db_resps: List[SensorHealthMonitoringDevice] | DB_Error = get_all_sensor_devices(
            )
            if not isinstance(db_resps, SensorHealthMonitoringDevice):
                sensor_devices: List[SensorHealthMonitoringDeviceType] = [
                    serialize(sensor_device) for sensor_device in db_resps]
                return jsonify(sensor_devices), 200
            else:
                return jsonify(db_resps), 400
        except Exception as e:
            return jsonify({"api_error": str(e)}), 500
    else:
        try:
            db_resp: SensorHealthMonitoringDevice | DB_Error = get_sensor_device(
                code)
            if isinstance(db_resp, SensorHealthMonitoringDevice):
                sensor_device: SensorHealthMonitoringDeviceType = serialize(
                    db_resp)
                return jsonify(sensor_device), 200
            else:
                return jsonify(db_resp), 400
        except Exception as e:
            return jsonify({"api_error": str(e)}), 500


@login_authorisation
def get_all_by_shipment(shipment: str) -> tuple[Response, int] | tuple[API_Error, int]:
    try:
        db_resps: List[SensorHealthMonitoringDevice] | DB_Error = get_all_sensor_device_by_shipment(shipment=shipment
                                                                                                    )
        if not isinstance(db_resps, SensorHealthMonitoringDevice):
            sensor_devices: List[SensorHealthMonitoringDeviceType] = [
                serialize(sensor_device) for sensor_device in db_resps]
            return jsonify(sensor_devices), 200
        else:
            return jsonify(db_resps), 400
    except Exception as e:
        return jsonify({"api_error": str(e)}), 500


@login_authorisation
def create_or_update() -> tuple[Response, int] | tuple[API_Error, int]:
    data = request.get_json()
    if not data:
        return jsonify({"api_error": "No JSON data provided"}), 400

    sensor_device: SensorHealthMonitoringDeviceType = SensorHealthMonitoringDeviceType(
        code=data.get("code"),
        shipment=data.get("shipment"),
        description=data.get("description")
    )
    if not sensor_device:
        return jsonify({"api_error": "Sensor device details not provided"}), 400

    try:
        if request.method == "PUT":
            db_resp: SensorHealthMonitoringDevice | DB_Error = update_sensor_device(
                sensor_device_details=sensor_device)
        else:
            db_resp: SensorHealthMonitoringDevice | DB_Error = create_sensor_device(
                sensor_device_details=sensor_device)

        if isinstance(db_resp, SensorHealthMonitoringDevice):
            sensor_device: SensorHealthMonitoringDeviceType = serialize(
                db_resp)
            return jsonify(sensor_device), 200
        else:
            return jsonify(db_resp), 400
    except Exception as e:
        return jsonify({"api_error": str(e)}), 500


@login_authorisation
def delete(code: str) -> tuple[Response, int] | tuple[API_Error, int]:
    try:
        db_resp: SensorHealthMonitoringDevice | DB_Error = delete_sensor_device(
            code)
        if isinstance(db_resp, SensorHealthMonitoringDevice):
            sensor_device: SensorHealthMonitoringDeviceType = serialize(
                db_resp)
            return jsonify(sensor_device), 200
        else:
            return jsonify(db_resp), 400
    except Exception as e:
        return {"api_error": str(e)}, 500
