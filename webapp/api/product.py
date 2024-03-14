from flask import request, jsonify
from models.product import *
from database.product import *


def get(code: str):
    if code.casefold() == "all":
        try:
            products: List[Product] = get_all_products()
            return jsonify(products), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 400
    else:
        try:
            product: Product = get_product(code)
            return jsonify(product), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 400


def create_or_update():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No JSON data provided"}), 400

    code = data.get("code")
    if not code:
        return jsonify({"error": "Product code is required"}), 400
    name = data.get("name")
    if not name:
        return jsonify({"error": "Product name is required"}), 400

    try:
        product: Product = create_or_update_product(code, name)
        return jsonify(product), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


def delete(code: str):
    try:
        product: Product = delete_product(code)
        return jsonify(product), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
