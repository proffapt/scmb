from . import db
from typing import List
from models.error import DB_Error
from models.certificate import Certificate
from models.shipment_event import ShipmentEvent
from models.shipment import Shipment, ShipmentType
from models.shipment_metadata import ShipmentMetadata


def get_all_shipments() -> List[Shipment] | DB_Error:
    try:
        shipments: List[Shipment] = Shipment.query.all()
        return shipments
    except Exception as e:
        return {"db_error": str(e)}


def get_all_shipments_by_supplychain(supplychain: int) -> List[Shipment] | DB_Error:
    try:
        shipments: List[Shipment] = Shipment.query.filter_by(
            supplychain=supplychain).all()
        return shipments
    except Exception as e:
        return {"db_error": str(e)}


def get_all_shipments_by_product(product: str) -> List[Shipment] | DB_Error:
    try:
        shipments: List[Shipment] = Shipment.query.filter_by(
            product=product).all()
        return shipments
    except Exception as e:
        return {"db_error": str(e)}


def get_all_shipments_by_supplychain_and_product(supplychain: int, product: str) -> List[Shipment] | DB_Error:
    try:
        shipments: List[Shipment] = Shipment.query.filter_by(
            supplychain=supplychain, product=product).all()
        return shipments
    except Exception as e:
        return {"db_error": str(e)}


def get_shipment(code: str) -> Shipment | DB_Error:
    try:
        shipment: Shipment = Shipment.query.filter_by(code=code).first()
        if shipment:
            return shipment
        else:
            return {"db_error": "Shipment not found"}
    except Exception as e:
        return {"db_error": str(e)}


def create_shipment(shipment_details: ShipmentType) -> Shipment | DB_Error:
    try:
        check_shipment: Shipment | DB_Error = get_shipment(
            shipment_details.get("code"))
        if isinstance(check_shipment, Shipment):
            return {"db_error": "Shipment already exists"}
        else:
            shipment = Shipment(
                code=shipment_details.get("code"),
                supplychain=shipment_details.get("supplychain"),
                product=shipment_details.get("product"),
                quantity=shipment_details.get("quantity"),
                quantity_unit=shipment_details.get("quantity_unit"),
                acceptable_quality_lower_bound=shipment_details.get(
                    "acceptable_quality_lower_bound"),
                acceptable_quality_upper_bound=shipment_details.get(
                    "acceptable_quality_upper_bound"),
                expected_quality=shipment_details.get("expected_quality")
            )
            db.session.add(shipment)
            db.session.commit()
            return shipment
    except Exception as e:
        return {"db_error": str(e)}


def update_shipment(shipment_details: ShipmentType) -> Shipment | DB_Error:
    try:
        shipment: Shipment | DB_Error = get_shipment(
            shipment_details.get("code"))
        if isinstance(shipment, Shipment):
            shipment.supplychain = shipment_details.get("supplychain")
            shipment.product = shipment_details.get("product")
            shipment.quantity = shipment_details.get("quantity")
            shipment.quantity_unit = shipment_details.get("quantity_unit")
            shipment.acceptable_quality_lower_bound = shipment_details.get(
                "acceptable_quality_lower_bound")
            shipment.acceptable_quality_upper_bound = shipment_details.get(
                "acceptable_quality_upper_bound")
            shipment.expected_quality = shipment_details.get(
                "expected_quality")
            db.session.commit()
            return shipment
        else:
            return shipment
    except Exception as e:
        return {"db_error": str(e)}


def delete_shipment(code: str) -> Shipment | DB_Error:
    try:
        shipment: Shipment | DB_Error = get_shipment(code)
        if isinstance(shipment, Shipment):
            # Delete the connected entries in Shipment_Metadata, Shipment_Event and Certificate tables
            db.session.query(ShipmentMetadata).filter(ShipmentMetadata.shipment == code).delete()
            db.session.query(ShipmentEvent).filter(ShipmentEvent.shipment == code).delete()
            db.session.query(Certificate).filter(Certificate.shipment == code).delete()
            # Delete the shipment entry
            db.session.delete(shipment)
            # Commit the changes
            db.session.commit()
            return shipment
        else:
            return shipment
    except Exception as e:
        return {"db_error": str(e)}
