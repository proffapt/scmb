import os
import jwt
import bcrypt
from models.person import Person
from database.person import get_person
from datetime import datetime, timedelta, UTC
from flask import Response, jsonify, request
from models.error import API_Error, DB_Error, LOGIN_Error


def generate_jwt(username: str):
    payload = {
        'sub': username,
        'exp': datetime.now(UTC) + timedelta(hours=1),
        'iat': datetime.now(UTC) - timedelta(seconds=10)
    }

    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")
    token = jwt.encode(payload, JWT_SECRET_KEY, algorithm='HS256')

    return token


def login() -> tuple[Response, int] | tuple[API_Error, int] | tuple[LOGIN_Error, int]:
    data = request.get_json()
    if not data:
        return jsonify({"api_error": "No JSON data provided"}), 400

    try:
        username = data.get("username")
        person: Person | DB_Error = get_person(username)
        if not isinstance(person, Person):
            return jsonify({"login_error": "username or password incorrect"}), 404
        else:
            HASH_SALT = os.environ.get("HASH_SALT")
            if not HASH_SALT:
                return jsonify({"api_error": "Hash salt not found"}), 500

            password = data.get("password")
            hashed_provided_pass = bcrypt.hashpw(password.encode(
                'utf-8'), HASH_SALT.encode("utf-8")).decode('utf-8')

            if hashed_provided_pass == person.password:
                token = generate_jwt(username)
                return jsonify({'jwt_token': token}), 200
            else:
                return jsonify({"login_error": "username or password incorrect"}), 404
    except Exception as e:
        return jsonify({"api_error": str(e)}), 500
