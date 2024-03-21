from flask import Blueprint
from . import product, shipment_metadata, supplychain, shipment

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

# Endpoints related to metadata of shipments
api.add_url_rule(
    "/metadata/<string:id>",
    view_func=shipment_metadata.get,
    methods=["GET"],
    endpoint="get_metadata"
)
api.add_url_rule(
    "/metadata/shipment/<string:code>",
    view_func=shipment_metadata.get_all_by_shipment,
    methods=["GET"],
    endpoint="get_metadata_by_shipment"
)
api.add_url_rule(
    "/metadata/<int:id>",
    view_func=shipment_metadata.delete,
    methods=["DELETE"],
    endpoint="delete_metadata"
)
api.add_url_rule(
    "/metadata",
    view_func=shipment_metadata.create_or_update,
    methods=["POST", "PUT"],
    endpoint="create_or_update_metadata"
)
