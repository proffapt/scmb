from flask import Blueprint
from . import product, supplychain

api = Blueprint('api', __name__)

# Endpoints related to product
api.add_url_rule(
    "/product/<string:code>",
    view_func=product.get,
    methods=["GET"],
    endpoint="get_product"
)
api.add_url_rule(
    "/product/<string:code>",
    view_func=product.delete,
    methods=["DELETE"],
    endpoint="delete_product"
)
api.add_url_rule(
    "/product",
    view_func=product.create_or_update,
    methods=["POST", "PUT"],
    endpoint="create_or_update_product"
)

# Endpoints related to supply_chain
api.add_url_rule(
    "/sc/<string:id>",
    view_func=supplychain.get,
    methods=["GET"],
    endpoint="get_supply_chain"
)
api.add_url_rule(
    "/sc/<int:id>",
    view_func=supplychain.delete,
    methods=["DELETE"],
    endpoint="delete_supply_chain"
)
api.add_url_rule(
    "/sc",
    view_func=supplychain.create_or_update,
    methods=["POST", "PUT"],
    endpoint="create_or_update_supply_chain"
)
