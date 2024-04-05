from database import db
from typing import TypedDict


class Role(db.Model):
    username = db.Column(db.String(50), db.ForeignKey(
        'person.username'), nullable=False)
    role = db.Column(db.String(50), db.ForeignKey(
        'rolesmap.role'), nullable=False)


class RoleType(TypedDict):
    username: str
    role: str


def serialize(role: Role) -> RoleType:
    return {
        "username": role.username,
        "role": role.role
    }
