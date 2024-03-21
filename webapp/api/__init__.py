from flask import Blueprint
from . import (
    product,
    shipment_metadata,
    supplychain,
    shipment,
    shipment_event,
    person,
    certificate
)

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

# Endpoints related to metadata of shipment
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

# Endpoints related to events of shipment
api.add_url_rule(
    "/event/<string:id>",
    view_func=shipment_event.get,
    methods=["GET"],
    endpoint="get_events"
)
api.add_url_rule(
    "/event/shipment/<string:code>",
    view_func=shipment_event.get_all_by_shipment,
    methods=["GET"],
    endpoint="get_events_by_shipment"
)
api.add_url_rule(
    "/event/<int:id>",
    view_func=shipment_event.delete,
    methods=["DELETE"],
    endpoint="delete_events"
)
api.add_url_rule(
    "/event",
    view_func=shipment_event.create_or_update,
    methods=["POST", "PUT"],
    endpoint="create_or_update_events"
)

# Endpoints related to person
api.add_url_rule(
    "/person/<string:username>",
    view_func=person.get,
    methods=["GET"],
    endpoint="get_person"
)
api.add_url_rule(
    "/person/<string:username>",
    view_func=person.delete,
    methods=["DELETE"],
    endpoint="delete_person"
)
api.add_url_rule(
    "/person",
    view_func=person.create_or_update,
    methods=["POST", "PUT"],
    endpoint="create_or_update_person"
)

# Endpoints related to certificates
api.add_url_rule(
    "/certificate/<string:id>",
    view_func=certificate.get,
    methods=["GET"],
    endpoint="get_certificate"
)
api.add_url_rule(
    "/certificate/shipment/<string:code>",
    view_func=certificate.get_all_by_shipment,
    methods=["GET"],
    endpoint="get_certificates_by_shipment"
)
api.add_url_rule(
    "/certificate/issuer/<string:username>",
    view_func=certificate.get_all_by_issuer,
    methods=["GET"],
    endpoint="get_certificates_by_issuer"
)
api.add_url_rule(
    "/certificate/<int:id>/download",
    view_func=certificate.download,
    methods=["GET"],
    endpoint="download_certificate"
)
api.add_url_rule(
    "/certificate/<int:id>",
    view_func=certificate.delete,
    methods=["DELETE"],
    endpoint="delete_certificate"
)
api.add_url_rule(
    "/certificate",
    view_func=certificate.create_or_update,
    methods=["POST", "PUT"],
    endpoint="create_or_update_certificate"
)
