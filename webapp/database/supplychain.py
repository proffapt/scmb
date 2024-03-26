from . import db
from typing import List
from models.supplychain import *
from models.error import DB_Error
from models.shipment import Shipment
from database.shipment import delete_shipment, get_all_shipments_by_supplychain


def get_all_supply_chains() -> List[Supplychain] | DB_Error:
    try:
        supplychain: List[Supplychain] = Supplychain.query.all()
        return supplychain
    except Exception as e:
        return {"db_error": str(e)}


def get_supply_chain(id: int) -> Supplychain | DB_Error:
    try:
        supplychain: Supplychain = Supplychain.query.get(id)
        if supplychain:
            return supplychain
        else:
            return {"db_error": "Supply Chain not found"}
    except Exception as e:
        return {"db_error": str(e)}


def create_supply_chain(name: str) -> Supplychain | DB_Error:
    try:
        supplychain: Supplychain = Supplychain(name=name)
        db.session.add(supplychain)
        db.session.commit()
        return supplychain
    except Exception as e:
        return {"db_error": str(e)}


def update_supply_chain(id: int, name: str) -> Supplychain | DB_Error:
    try:
        supplychain: Supplychain | DB_Error = get_supply_chain(id)
        if isinstance(supplychain, Supplychain):
            supplychain.name = name
            db.session.commit()
            return supplychain
        else:
            return supplychain
    except Exception as e:
        return {"db_error": str(e)}


def delete_supply_chain(id: int) -> Supplychain | DB_Error:
    try:
        supplychain: Supplychain | DB_Error = get_supply_chain(id)
        if isinstance(supplychain, Supplychain):
            # TODO: Delete the connected Role table entries
            # Delete the connected entries in Shipment table
            shipments: List[Shipment] | DB_Error = get_all_shipments_by_supplychain(
                id)
            for shipment in shipments:
                if isinstance(shipment, Shipment):
                    delete_shipment(shipment.code)
            # Delete the supplychain entry
            db.session.delete(supplychain)
            # Commit the changes
            db.session.commit()
            return supplychain
        else:
            return supplychain
    except Exception as e:
        return {"db_error": str(e)}
