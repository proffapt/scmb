from datetime import datetime
import os
import jwt
from models.person import Person
from models.error import DB_Error
from flask import jsonify, request
from database.person import get_person


def login_authorisation(func):
    def wrapper(*args, **kwargs):
        # Check if the token was sent with the request
        token = None
        if "Authorization" in request.headers:
            token = request.headers["Authorization"].split(" ")[1]
        if not token:
            return jsonify({"auth_error": "Authentication token not provided"}), 401
        try:
            # Now that we have the token, let's validate it
            JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")
            token_data = jwt.decode(
                token, JWT_SECRET_KEY, algorithms=["HS256"])

            alleged_username = token_data["sub"]
            if not alleged_username:
                return jsonify({"auth_error": "Invalid authentication token"})
            alleged_user: Person | DB_Error = get_person(alleged_username)

            if not isinstance(alleged_user, Person):
                return jsonify({"auth_error": "Invalid authentication token"})
        except Exception as e:
            return jsonify({"auth_error": str(e)}), 500

        return func(*args, **kwargs)

    return wrapper
