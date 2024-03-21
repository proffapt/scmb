from flask import Blueprint
from . import product, supplychain, shipment

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

# Endpoints related to shipment
api.add_url_rule(
    "/shipment/<string:code>",
    view_func=shipment.get,
    methods=["GET"],
    endpoint="get_shipment"
)
api.add_url_rule(
    "/shipment/sc/<int:id>",
    view_func=shipment.get_all_by_supplychain,
    methods=["GET"],
    endpoint="get_all_shipment_of_supplychain"
)
api.add_url_rule(
    "/shipment/product/<string:code>",
    view_func=shipment.get_all_by_product,
    methods=["GET"],
    endpoint="get_all_shipment_of_product"
)
api.add_url_rule(
    "/shipment/sc/<int:id>/product/<string:code>",
    view_func=shipment.get_all_by_supplychain_product,
    methods=["GET"],
    endpoint="get_all_shipment_of_product_and_supplychain"
)
api.add_url_rule(
    "/shipment/<string:code>",
    view_func=shipment.delete,
    methods=["DELETE"],
    endpoint="delete_shipment"
)
api.add_url_rule(
    "/shipment",
    view_func=shipment.create_or_update,
    methods=["POST", "PUT"],
    endpoint="create_or_update_shipment"
)
