from models.error import API_Error
from models.person import *
from database.person import *
from flask import Response, request, jsonify
from middleware.auth import login_authorisation


@login_authorisation
def get(username: str) -> tuple[Response, int] | tuple[API_Error, int]:
    if username.casefold() == "all":
        try:
            db_resps: List[Person] | DB_Error = get_all_persons()
            if not isinstance(db_resps, Person):
                persons: List[PersonType] = [
                    serialize(person) for person in db_resps]
                return jsonify(persons), 200
            else:
                return jsonify(db_resps), 400
        except Exception as e:
            return jsonify({"api_error": str(e)}), 500
    else:
        try:
            db_resp: Person | DB_Error = get_person(username)
            if isinstance(db_resp, Person):
                person: PersonType = serialize(db_resp)
                return jsonify(person), 200
            else:
                return jsonify(db_resp), 400
        except Exception as e:
            return jsonify({"api_error": str(e)}), 500


# User creation (aka signup) shouldn't require any authorisation
def create() -> tuple[Response, int] | tuple[API_Error, int]:
    data = request.get_json()
    if not data:
        return jsonify({"api_error": "No JSON data provided"}), 400

    person_details: PersonType = PersonType(
        username=data.get("username"),
        email=data.get("email"),
        password=data.get("password"),
        first_name=data.get("first_name"),
        last_name=data.get("last_name"),
        address=data.get("address"),
        phone=data.get("phone"),
        organisation=data.get("organisation"),
    )
    if not person_details:
        return jsonify({"api_error": "Person details not provided"}), 400

    try:
        db_resp: Person | DB_Error = create_person(
            person_details=person_details)

        if isinstance(db_resp, Person):
            person: PersonType = serialize(db_resp)
            return jsonify(person), 200
        else:
            return jsonify(db_resp), 400
    except Exception as e:
        return jsonify({"api_error": str(e)}), 500


@login_authorisation
def update() -> tuple[Response, int] | tuple[API_Error, int]:
    data = request.get_json()
    if not data:
        return jsonify({"api_error": "No JSON data provided"}), 400

    person_details: PersonType = PersonType(
        username=data.get("username"),
        email=data.get("email"),
        password=data.get("password"),
        first_name=data.get("first_name"),
        last_name=data.get("last_name"),
        address=data.get("address"),
        phone=data.get("phone"),
        organisation=data.get("organisation"),
    )
    if not person_details:
        return jsonify({"api_error": "Person details not provided"}), 400

    try:
        db_resp: Person | DB_Error = update_person(
            person_details=person_details)

        if isinstance(db_resp, Person):
            person: PersonType = serialize(db_resp)
            return jsonify(person), 200
        else:
            return jsonify(db_resp), 400
    except Exception as e:
        return jsonify({"api_error": str(e)}), 500


@login_authorisation
def delete(username: str) -> tuple[Response, int] | tuple[API_Error, int]:
    try:
        db_resp: Person | DB_Error = delete_person(username)
        if isinstance(db_resp, Person):
            person_info: PersonType = serialize(db_resp)
            return jsonify(person_info), 200
        else:
            return jsonify(db_resp), 400
    except Exception as e:
        return jsonify({"api_error": str(e)}), 500
