from .product import *
from flask import Blueprint

api = Blueprint('api', __name__)

# Endpoints related to product
api.add_url_rule("/product/<string:code>",
                 view_func=get, methods=["GET"])
api.add_url_rule("/product/<string:code>",
                 view_func=delete, methods=["DELETE"])
api.add_url_rule("/product", view_func=create_or_update,
                 methods=["POST", "PUT"])
