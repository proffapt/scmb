from models.shipment import *
from database.shipment import *
from models.error import API_Error
from flask import Response, request, jsonify
from middleware.auth import login_authorisation


@login_authorisation
def get(code: str) -> tuple[Response, int] | tuple[API_Error, int]:
    if code.casefold() == "all":
        try:
            db_resps: List[Shipment] | DB_Error = get_all_shipments()
            if not isinstance(db_resps, Shipment):
                shipments: List[ShipmentType] = [
                    serialize(shipment) for shipment in db_resps]
                return jsonify(shipments), 200
            else:
                return jsonify(db_resps), 400
        except Exception as e:
            return jsonify({"api_error": str(e)}), 500
    else:
        try:
            db_resp: Shipment | DB_Error = get_shipment(code)
            if isinstance(db_resp, Shipment):
                shipment: ShipmentType = serialize(db_resp)
                return jsonify(shipment), 200
            else:
                return jsonify(db_resp), 400
        except Exception as e:
            return jsonify({"api_error": str(e)}), 500


@login_authorisation
def get_all_by_product(code: str) -> tuple[Response, int] | tuple[API_Error, int]:
    try:
        db_resps: List[Shipment] | DB_Error = get_all_shipments_by_product(
            code)
        if not isinstance(db_resps, Shipment):
            shipments: List[ShipmentType] = [
                serialize(shipment) for shipment in db_resps]
            return jsonify(shipments), 200
        else:
            return jsonify(db_resps), 400
    except Exception as e:
        return jsonify({"api_error": str(e)}), 500


@login_authorisation
def get_all_by_supplychain(id: int) -> tuple[Response, int] | tuple[API_Error, int]:
    try:
        db_resps: List[Shipment] | DB_Error = get_all_shipments_by_supplychain(
            id)
        if not isinstance(db_resps, Shipment):
            shipments: List[ShipmentType] = [
                serialize(shipment) for shipment in db_resps]
            return jsonify(shipments), 200
        else:
            return jsonify(db_resps), 400
    except Exception as e:
        return jsonify({"api_error": str(e)}), 500


@login_authorisation
def get_all_by_supplychain_product(id: int, code: str) -> tuple[Response, int] | tuple[API_Error, int]:
    try:
        db_resps: List[Shipment] | DB_Error = get_all_shipments_by_supplychain_and_product(
            id, code)
        if not isinstance(db_resps, Shipment):
            shipments: List[ShipmentType] = [
                serialize(shipment) for shipment in db_resps]
            return jsonify(shipments), 200
        else:
            return jsonify(db_resps), 400
    except Exception as e:
        return jsonify({"api_error": str(e)}), 500


@login_authorisation
def create_or_update() -> tuple[Response, int] | tuple[API_Error, int]:
    data = request.get_json()
    if not data:
        return jsonify({"api_error": "No JSON data provided"}), 400

    shipment: ShipmentType = ShipmentType(
        code=data.get("code"),
        supplychain=data.get("supplychain"),
        product=data.get("product"),
        quantity=data.get("quantity"),
        quantity_unit=data.get("quantity_unit"),
        acceptable_quality_lower_bound=data.get(
            "acceptable_quality_lower_bound"),
        acceptable_quality_upper_bound=data.get(
            "acceptable_quality_upper_bound"),
        expected_quality=data.get("expected_quality")
    )
    if not shipment:
        return jsonify({"api_error": "Shipment details not provided"}), 400

    try:
        if request.method == "PUT":
            db_resp: Shipment | DB_Error = update_shipment(
                shipment_details=shipment)
        else:
            db_resp: Shipment | DB_Error = create_shipment(
                shipment_details=shipment)

        if isinstance(db_resp, Shipment):
            shipment: ShipmentType = serialize(db_resp)
            return jsonify(shipment), 200
        else:
            return jsonify(db_resp), 400
    except Exception as e:
        return jsonify({"api_error": str(e)}), 500


@login_authorisation
def delete(code: str) -> tuple[Response, int] | tuple[API_Error, int]:
    try:
        db_resp: Shipment | DB_Error = delete_shipment(code)
        if isinstance(db_resp, Shipment):
            shipment: ShipmentType = serialize(db_resp)
            return jsonify(shipment), 200
        else:
            return jsonify(db_resp), 400
    except Exception as e:
        return {"api_error": str(e)}, 500
