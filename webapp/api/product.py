from models.product import *
from database.product import *
from models.error import API_Error
from flask import Response, request, jsonify


def get(code: str) -> tuple[Response, int] | tuple[API_Error, int]:
    if code.casefold() == "all":
        try:
            products = [serialize(product) for product in get_all_products()]
            return jsonify(products), 200
        except Exception as e:
            return jsonify({"api_error": str(e)}), 400
    else:
        try:
            product = serialize(get_product(code))
            return jsonify(product), 200
        except Exception as e:
            return jsonify({"api_error": str(e)}), 400


def create_or_update() -> tuple[Response, int] | tuple[API_Error, int]:
    data = request.get_json()
    if not data:
        return jsonify({"api_error": "No JSON data provided"}), 400

    code = data.get("code")
    name = data.get("name")
    if not code or not name:
        return jsonify({"api_error": "Product code and name are required"}), 400

    try:
        product = create_or_update_product(code, name)
        return jsonify(product), 200
    except Exception as e:
        return jsonify({"api_error": str(e)}), 500


def delete(code: str) -> tuple[Response, int] | tuple[API_Error, int]:
    try:
        product: Product | DB_Error = delete_product(code)
        product: ProductType = serialize(product)
        return jsonify(product), 200
    except Exception as e:
        return {"api_error": str(e)}, 500
