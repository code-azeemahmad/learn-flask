from marshmallow import Schema, fields


class UserResponseSchema(Schema):

    id = fields.Integer(dump_only=True)

    email = fields.Email()

    role = fields.String()


user_response_schema = UserResponseSchema()
users_response_schema = UserResponseSchema(many=True)