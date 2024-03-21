from . import db
from typing import List
from datetime import datetime
from models.error import DB_Error
from models.shipment_event import ShipmentEvent, ShipmentEventType


def get_all_events() -> List[ShipmentEvent] | DB_Error:
    try:
        events: List[ShipmentEvent] = ShipmentEvent.query.all()
        return events
    except Exception as e:
        return {"db_error": str(e)}


def get_all_events_by_shipment(shipment: str) -> List[ShipmentEvent] | DB_Error:
    try:
        events: List[ShipmentEvent] = ShipmentEvent.query.filter_by(
            shipment=shipment).all()
        return events
    except Exception as e:
        return {"db_error": str(e)}


def get_event(id: int) -> ShipmentEvent | DB_Error:
    try:
        event: ShipmentEvent = ShipmentEvent.query.get(id)
        if event:
            return event
        else:
            return {"db_error": "Shipment Event not found"}
    except Exception as e:
        return {"db_error": str(e)}


def create_event(event_details: ShipmentEventType) -> ShipmentEvent | DB_Error:
    try:
        event: ShipmentEvent = ShipmentEvent(
            timestamp=datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
            shipment=event_details.get("shipment"),
            event=event_details.get("event")
        )
        db.session.add(event)
        db.session.commit()
        return event
    except Exception as e:
        return {"db_error": str(e)}


def update_event(event_details: ShipmentEventType) -> ShipmentEvent | DB_Error:
    try:
        event_id = event_details.get("id")
        event: ShipmentEvent | DB_Error = get_event(event_id)
        if isinstance(event, ShipmentEvent):
            event.timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
            event.shipment = event_details.get("shipment")
            event.event = event_details.get("event")
            db.session.commit()
            return event
        else:
            return event
    except Exception as e:
        return {"db_error": str(e)}


def delete_event(id: int) -> ShipmentEvent | DB_Error:
    try:
        event: ShipmentEvent | DB_Error = get_event(id)
        if isinstance(event, ShipmentEvent):
            db.session.delete(event)
            db.session.commit()
            return event
        else:
            return event
    except Exception as e:
        return {"db_error": str(e)}
