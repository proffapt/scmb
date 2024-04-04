from models.product import *
from database.product import *
from models.error import API_Error
from flask import Response, request, jsonify
from middleware.auth import login_authorisation


@login_authorisation
def get(code: str) -> tuple[Response, int] | tuple[API_Error, int]:
    if code.casefold() == "all":
        try:
            db_resps: List[Product] | DB_Error = get_all_products()
            if not isinstance(db_resps, Product):
                products: List[ProductType] = [
                    serialize(product) for product in db_resps]
                return jsonify(products), 200
            else:
                return jsonify(db_resps), 400
        except Exception as e:
            return jsonify({"api_error": str(e)}), 500
    else:
        try:
            db_resp: Product | DB_Error = get_product(code)
            if isinstance(db_resp, Product):
                product: ProductType = serialize(db_resp)
                return jsonify(product), 200
            else:
                return jsonify(db_resp), 400
        except Exception as e:
            return jsonify({"api_error": str(e)}), 500


@login_authorisation
def create_or_update() -> tuple[Response, int] | tuple[API_Error, int]:
    data = request.get_json()
    if not data:
        return jsonify({"api_error": "No JSON data provided"}), 400

    code = data.get("code")
    name = data.get("name")
    if not code or not name:
        return jsonify({"api_error": "Product code and name are required"}), 400

    try:
        if request.method == "PUT":
            db_resp: Product | DB_Error = update_product(code, name)
        else:
            db_resp: Product | DB_Error = create_product(code, name)

        if isinstance(db_resp, Product):
            product: ProductType = serialize(db_resp)
            return jsonify(product), 200
        else:
            return jsonify(db_resp), 400
    except Exception as e:
        return jsonify({"api_error": str(e)}), 500


@login_authorisation
def delete(code: str) -> tuple[Response, int] | tuple[API_Error, int]:
    try:
        db_resp: Product | DB_Error = delete_product(code)
        if isinstance(db_resp, Product):
            product: ProductType = serialize(db_resp)
            return jsonify(product), 200
        else:
            return jsonify(db_resp), 400
    except Exception as e:
        return {"api_error": str(e)}, 500
