from flask import Blueprint, request, jsonify

from app.schemas.user_schema import user_schema
from app.services.user_service import UserService
from app.schemas.response_schema import (
    user_response_schema,
    users_response_schema
)

from flask_login import login_user


auth_bp = Blueprint(
    "auth",
    __name__,
    url_prefix="/auth"
)


@auth_bp.route("/register", methods=["POST"])
def register():

    data = request.get_json()

    validated_data = user_schema.load(data)

    user = UserService.register(validated_data)

    return jsonify({
        "message": "User registered successfully.",
        "user": user_response_schema.dump(user)
    }), 201


@auth_bp.route("/login", methods=["POST"])
def login():

    validated_data = user_schema.load(request.get_json())

    user = UserService.login(validated_data)

    login_user(user)

    return jsonify({
        "message": "Login successful.",
        "user": user_response_schema.dump(user)
    }), 200



'''
HTTP is stateless; each request is independent.
Applications need a way to associate multiple requests with the same user.
A session stores authentication state on the server.
A cookie stores a session identifier in the browser.
The browser automatically sends the cookie with future requests, allowing the server to recognize the user.
'''
from flask import Blueprint, request, jsonify