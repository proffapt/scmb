from models.supplychain import *
from database.supplychain import *
from models.error import API_Error
from flask import Response, request, jsonify
from middleware.auth import login_authorisation


@login_authorisation
def get(id: int | str) -> tuple[Response, int] | tuple[API_Error, int]:
    if isinstance(id, str) and id.casefold() == "all":
        try:
            db_resps: List[Supplychain] | DB_Error = get_all_supply_chains()
            if not isinstance(db_resps, Supplychain):
                supplychains: List[SupplychainType] = [
                    serialize(supplychain) for supplychain in db_resps]
                return jsonify(supplychains), 200
            else:
                return jsonify(db_resps), 400
        except Exception as e:
            return jsonify({"api_error": str(e)}), 500
    else:
        try:
            db_resp: Supplychain | DB_Error = get_supply_chain(int(id))
            if isinstance(db_resp, Supplychain):
                supplychain: SupplychainType = serialize(db_resp)
                return jsonify(supplychain), 200
            else:
                return jsonify(db_resp), 400
        except Exception as e:
            return jsonify({"api_error": str(e)}), 500


@login_authorisation
def create_or_update() -> tuple[Response, int] | tuple[API_Error, int]:
    data = request.get_json()
    if not data:
        return jsonify({"api_error": "No JSON data provided"}), 400

    name = data.get("name")
    if not name:
        return jsonify({"api_error": "Supply Chain name is required"}), 400

    try:
        if request.method == "PUT":
            id = data.get("id")
            if not id:
                return jsonify({"api_error": "Supply Chain id is required to update"}), 400
            db_resp: Supplychain | DB_Error = update_supply_chain(id, name)
        else:
            db_resp: Supplychain | DB_Error = create_supply_chain(name)

        if isinstance(db_resp, Supplychain):
            supplychain: SupplychainType = serialize(db_resp)
            return jsonify(supplychain), 200
        else:
            return jsonify(db_resp), 400
    except Exception as e:
        return jsonify({"api_error": str(e)}), 500


@login_authorisation
def delete(id: int) -> tuple[Response, int] | tuple[API_Error, int]:
    try:
        db_resp: Supplychain | DB_Error = delete_supply_chain(id)
        if isinstance(db_resp, Supplychain):
            supplychain: SupplychainType = serialize(db_resp)
            return jsonify(supplychain), 200
        else:
            return jsonify(db_resp), 400
    except Exception as e:
        return jsonify({"api_error": str(e)}), 500
