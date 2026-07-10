from flask import Blueprint, request, jsonify

from app.schemas.user_schema import user_schema
from app.services.user_service import UserService


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
        "user": {
            "id": user.id,
            "email": user.email,
            "role": user.role
        }
    }), 201


'''
HTTP is stateless; each request is independent.
Applications need a way to associate multiple requests with the same user.
A session stores authentication state on the server.
A cookie stores a session identifier in the browser.
The browser automatically sends the cookie with future requests, allowing the server to recognize the user.
'''