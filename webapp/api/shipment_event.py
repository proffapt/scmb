from models.error import API_Error
from models.shipment_event import *
from database.shipment_event import *
from flask import Response, request, jsonify
from middleware.auth import login_authorisation


@login_authorisation
def get(id: int | str) -> tuple[Response, int] | tuple[API_Error, int]:
    if isinstance(id, str) and id.casefold() == "all":
        try:
            db_resps: List[ShipmentEvent] | DB_Error = get_all_events()
            if not isinstance(db_resps, ShipmentEvent):
                events: List[ShipmentEventType] = [
                    serialize(event) for event in db_resps]
                return jsonify(events), 200
            else:
                return jsonify(db_resps), 400
        except Exception as e:
            return jsonify({"api_error": str(e)}), 500
    else:
        try:
            db_resp: ShipmentEvent | DB_Error = get_event(int(id))
            if isinstance(db_resp, ShipmentEvent):
                event: ShipmentEventType = serialize(db_resp)
                return jsonify(event), 200
            else:
                return jsonify(db_resp), 400
        except Exception as e:
            return jsonify({"api_error": str(e)}), 500


@login_authorisation
def get_all_by_shipment(code: str) -> tuple[Response, int] | tuple[API_Error, int]:
    try:
        db_resps: List[ShipmentEvent] | DB_Error = get_all_events_by_shipment(
            code)
        if not isinstance(db_resps, ShipmentEvent):
            events: List[ShipmentEventType] = [
                serialize(event) for event in db_resps]
            return jsonify(events), 200
        else:
            return jsonify(db_resps), 400
    except Exception as e:
        return jsonify({"api_error": str(e)}), 500


@login_authorisation
def create_or_update() -> tuple[Response, int] | tuple[API_Error, int]:
    data = request.get_json()
    if not data:
        return jsonify({"api_error": "No JSON data provided"}), 400

    event: ShipmentEventType = ShipmentEventType(
        timestamp=data.get("timestamp"),
        shipment=data.get("shipment"),
        event=data.get("event")
    )
    if not event:
        return jsonify({"api_error": "Shipment Event details not provided"}), 400

    try:
        if request.method == "PUT":
            db_resp: ShipmentEvent | DB_Error = update_event(event)
        else:
            db_resp: ShipmentEvent | DB_Error = create_event(event)

        if isinstance(db_resp, ShipmentEvent):
            event_data: ShipmentEventType = serialize(db_resp)
            return jsonify(event_data), 200
        else:
            return jsonify(db_resp), 400
    except Exception as e:
        return jsonify({"api_error": str(e)}), 500


@login_authorisation
def delete(id: int) -> tuple[Response, int] | tuple[API_Error, int]:
    try:
        db_resp: ShipmentEvent | DB_Error = delete_event(id)
        if isinstance(db_resp, ShipmentEvent):
            event_data: ShipmentEventType = serialize(db_resp)
            return jsonify(event_data), 200
        else:
            return jsonify(db_resp), 400
    except Exception as e:
        return jsonify({"api_error": str(e)}), 500
