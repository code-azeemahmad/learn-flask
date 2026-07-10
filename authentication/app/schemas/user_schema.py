from marshmallow import Schema, fields, validate
from marshmallow import pre_load


class UserSchema(Schema):

    @pre_load
    def normalize(self, data, **kwargs):
        if not data:
            return {}

        # Normalize email
        if "email" in data and isinstance(data["email"], str):
            data["email"] = data["email"].strip().lower()

        # Normalize password
        if "password" in data and isinstance(data["password"], str):
            data["password"] = data["password"].strip()

        return data

    email = fields.Email(
        required=True,
        validate=validate.Length(
            max=254,
            error="Email must not exceed 254 characters."
        ),
        error_messages={
            "required": "Email is required.",
            "null": "Email cannot be null.",
            "invalid": "Please enter a valid email address."
        }
    )

    password = fields.String(
        required=True,
        validate=validate.Length(
            min=8,
            error="Password must be at least 8 characters long."
        ),
        error_messages={
            "required": "Password is required.",
            "null": "Password cannot be null.",
            "invalid": "Password must be a string."
        }
    )


user_schema = UserSchema()
users_schema = UserSchema(many=True)