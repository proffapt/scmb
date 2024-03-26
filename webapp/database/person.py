import os
import bcrypt
from database import db
from typing import List
from models.person import *
from models.error import DB_Error
from models.certificate import Certificate


def get_all_persons() -> List[Person] | DB_Error:
    try:
        persons: List[Person] = Person.query.all()
        return persons
    except Exception as e:
        return {"db_error": str(e)}


def get_person(username: str) -> Person | DB_Error:
    try:
        person: Person = Person.query.filter_by(username=username).first()
        if person:
            return person
        else:
            return {"db_error": "Person not found"}
    except Exception as e:
        return {"db_error": str(e)}


def create_person(person_details: PersonType) -> Person | DB_Error:
    try:
        HASH_SALT = os.environ.get("HASH_SALT")
        if not HASH_SALT:
            return {"db_error": "Hash salt not found"}

        person_username = person_details.get("username")
        if person_username == "all":
            return {"db_error": "Username can not be all"}

        person_password = person_details.get("password")
        # Hash the password before storing it
        hashed_password = bcrypt.hashpw(person_password.encode(
            'utf-8'), HASH_SALT.encode("utf-8")).decode('utf-8')

        person: Person = Person(
            username=person_username,
            email=person_details.get("email"),
            password=hashed_password,
            first_name=person_details.get("first_name"),
            last_name=person_details.get("last_name"),
            address=person_details.get("address"),
            phone=person_details.get("phone"),
            organisation=person_details.get("organisation"),
        )
        check_person: Person | DB_Error = get_person(person_username)
        if isinstance(check_person, Person):
            return {"db_error": "Username not available"}
        else:
            db.session.add(person)
            db.session.commit()
            return person
    except Exception as e:
        return {"db_error": str(e)}


def update_person(person_details: PersonType) -> Person | DB_Error:
    try:
        HASH_SALT = os.environ.get("HASH_SALT")
        if not HASH_SALT:
            return {"db_error": "Hash salt not found"}

        person_username = person_details.get("username")

        person_password = person_details.get("password")
        # Hash the password before storing it
        hashed_password = bcrypt.hashpw(person_password.encode(
            'utf-8'), HASH_SALT.encode("utf-8")).decode('utf-8')

        person: Person | DB_Error = get_person(username=person_username)
        if isinstance(person, Person):
            person.email = person_details.get("email")
            person.password = hashed_password
            person.first_name = person_details.get("first_name")
            person.last_name = person_details.get("last_name")
            person.address = person_details.get("address")
            person.phone = person_details.get("phone")
            person.organisation = person_details.get("organisation")
            db.session.commit()
            return person
        else:
            return person
    except Exception as e:
        return {"db_error": str(e)}


def delete_person(username: str) -> Person | DB_Error:
    try:
        person: Person | DB_Error = get_person(username)
        if isinstance(person, Person):
            # TODO: Also delete corresponding Person
            # Delete the connected entries in Certificate table
            db.session.query(Certificate).filter(
                Certificate.issuer == username).delete()
            # Delete the person entry
            db.session.delete(person)
            # Commit the changes
            db.session.commit()
            return person
        else:
            return person
    except Exception as e:
        return {"db_error": str(e)}
