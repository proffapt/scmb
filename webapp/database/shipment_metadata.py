from . import db
from typing import List
from datetime import datetime
from models.error import DB_Error
from models.shipment_metadata import ShipmentMetadata, ShipmentMetadataType


def get_all_metadata() -> List[ShipmentMetadata] | DB_Error:
    try:
        metadata: List[ShipmentMetadata] = ShipmentMetadata.query.all()
        return metadata
    except Exception as e:
        return {"db_error": str(e)}


def get_all_metadata_by_shipment(shipment: str) -> List[ShipmentMetadata] | DB_Error:
    try:
        metadata: List[ShipmentMetadata] = ShipmentMetadata.query.filter_by(
            shipment=shipment).all()
        return metadata
    except Exception as e:
        return {"db_error": str(e)}


def get_metadata(id: int) -> ShipmentMetadata | DB_Error:
    try:
        metadata: ShipmentMetadata = ShipmentMetadata.query.get(id)
        if metadata:
            return metadata
        else:
            return {"db_error": "Shipment Metadata not found"}
    except Exception as e:
        return {"db_error": str(e)}


def create_metadata(metadata_details: ShipmentMetadataType) -> ShipmentMetadata | DB_Error:
    try:
        metadata: ShipmentMetadata = ShipmentMetadata(
            timestamp=datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
            shipment=metadata_details.get("shipment"),
            latitude=metadata_details.get("latitude"),
            longitude=metadata_details.get("longitude"),
            temperature=metadata_details.get("temperature"),
            quality=metadata_details.get("quality")
        )
        db.session.add(metadata)
        db.session.commit()
        return metadata
    except Exception as e:
        return {"db_error": str(e)}


def update_metadata(metadata_details: ShipmentMetadataType) -> ShipmentMetadata | DB_Error:
    try:
        metadata_id = metadata_details.get("id")
        metadata: ShipmentMetadata | DB_Error = get_metadata(metadata_id)
        if isinstance(metadata, ShipmentMetadata):
            metadata.timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
            metadata.shipment = metadata_details.get("shipment")
            metadata.latitude = metadata_details.get("latitude")
            metadata.longitude = metadata_details.get("longitude")
            metadata.temperature = metadata_details.get("temperature")
            metadata.quality = metadata_details.get("quality")
            db.session.commit()
            return metadata
        else:
            return metadata
    except Exception as e:
        return {"db_error": str(e)}


def delete_metadata(id: int) -> ShipmentMetadata | DB_Error:
    try:
        metadata: ShipmentMetadata | DB_Error = get_metadata(id)
        if isinstance(metadata, ShipmentMetadata):
            db.session.delete(metadata)
            db.session.commit()
            return metadata
        else:
            return metadata
    except Exception as e:
        return {"db_error": str(e)}
