from models.error import API_Error
from models.shipment_metadata import *
from database.shipment_metadata import *
from flask import Response, request, jsonify
from middleware.auth import login_authorisation


@login_authorisation
def get(id: int | str) -> tuple[Response, int] | tuple[API_Error, int]:
    if isinstance(id, str) and id.casefold() == "all":
        try:
            db_resps: List[ShipmentMetadata] | DB_Error = get_all_metadata()
            if not isinstance(db_resps, ShipmentMetadata):
                metadatas: List[ShipmentMetadataType] = [
                    serialize(metadata) for metadata in db_resps]
                return jsonify(metadatas), 200
            else:
                return jsonify(db_resps), 400
        except Exception as e:
            return jsonify({"api_error": str(e)}), 500
    else:
        try:
            db_resp: ShipmentMetadata | DB_Error = get_metadata(int(id))
            if isinstance(db_resp, ShipmentMetadata):
                metadata: ShipmentMetadataType = serialize(db_resp)
                return jsonify(metadata), 200
            else:
                return jsonify(db_resp), 400
        except Exception as e:
            return jsonify({"api_error": str(e)}), 500


@login_authorisation
def get_all_by_shipment(code: str) -> tuple[Response, int] | tuple[API_Error, int]:
    try:
        db_resps: List[ShipmentMetadata] | DB_Error = get_all_metadata_by_shipment(
            code)
        if not isinstance(db_resps, ShipmentMetadata):
            metadatas: List[ShipmentMetadataType] = [
                serialize(metadata) for metadata in db_resps]
            return jsonify(metadatas), 200
        else:
            return jsonify(db_resps), 400
    except Exception as e:
        return jsonify({"api_error": str(e)}), 500


@login_authorisation
def create_or_update() -> tuple[Response, int] | tuple[API_Error, int]:
    data = request.get_json()
    if not data:
        return jsonify({"api_error": "No JSON data provided"}), 400

    metadata: ShipmentMetadataType = ShipmentMetadataType(
        shipment=data.get("shipment"),
        latitude=data.get("latitude"),
        longitude=data.get("longitude"),
        temperature=data.get("temperature"),
        quality=data.get("quality")
    )
    if not metadata:
        return jsonify({"api_error": "Shipment Metadata details not provided"}), 400

    try:
        if request.method == "PUT":
            db_resp: ShipmentMetadata | DB_Error = update_metadata(
                metadata_details=metadata)
        else:
            db_resp: ShipmentMetadata | DB_Error = create_metadata(
                metadata_details=metadata)

        if isinstance(db_resp, ShipmentMetadata):
            metadata: ShipmentMetadataType = serialize(db_resp)
            return jsonify(metadata), 200
        else:
            return jsonify(db_resp), 400
    except Exception as e:
        return jsonify({"api_error": str(e)}), 500


@login_authorisation
def delete(id: int) -> tuple[Response, int] | tuple[API_Error, int]:
    try:
        db_resp: ShipmentMetadata | DB_Error = delete_metadata(id)
        if isinstance(db_resp, ShipmentMetadata):
            metadata: ShipmentMetadataType = serialize(db_resp)
            return jsonify(metadata), 200
        else:
            return jsonify(db_resp), 400
    except Exception as e:
        return jsonify({"api_error": str(e)}), 500
