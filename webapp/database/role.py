from . import db
from typing import List
from models.role import Role
from models.error import DB_Error


def get_all_roles() -> List[Role] | DB_Error:
    try:
        products: List[Role] = Role.query.all()
        return products
    except Exception as e:
        return {"db_error": str(e)}


def get_person_role(username: str, role: str) -> List[Role] | DB_Error:
    try:
        roles: List[Role] = Role.query.filter_by(username=username).all()
        if roles:
            return roles
        else:
            return {"db_error": "No assigned role found for the user"}
    except Exception as e:
        return {"db_error": str(e)}


def give_person_role(username: str, role: str):
    pass


def update_person_role(username: str, role: str):
    pass


def delete_role(id: int) -> Role | DB_Error:
    try:
        role: Role | DB_Error = get_role(id)
        if isinstance(metadata, ShipmentMetadata):
            db.session.delete(metadata)
            db.session.commit()
            return metadata
        else:
            return metadata
    except Exception as e:
        return {"db_error": str(e)}
