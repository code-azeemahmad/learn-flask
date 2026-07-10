from marshmallow import Schema, fields, validate
from marshmallow import pre_load

# marshmallow do normalization using pre processing hooks

class StudentSchema(Schema):

    @pre_load
    def normalize(self, data, **kwargs):    # now you can delete app/validators/student_validator.py
        if not data:
            return {}

        # Normalize name
        if "name" in data and isinstance(data["name"], str):
            data["name"] = " ".join(data["name"].strip().split())

        # Normalize email
        if "email" in data and isinstance(data["email"], str):
            data["email"] = data["email"].strip().lower()

        # Normalize age
        if "age" in data:
            age = data["age"]

            if isinstance(age, str):
                age = age.strip()

                if age.isdigit():
                    data["age"] = int(age)

        return data

    # for custom rules, custom validators come in
    name = fields.String(
            required=True,
            validate=validate.Length(
                min=3,
                max=16,
                error="Name must be between 3 and 16 characters."
            ),
            error_messages={
                "required": "Name is required.",
                "null": "Name cannot be null.",
                "invalid": "Name must be a string."
            }
    )

    age = fields.Integer(
        required=True,
        validate=validate.Range(
            min=0,
            error="Age must be greater than or equal to 0."
        ),
        error_messages={
            "required": "Age is required.",
            "null": "Age cannot be null.",
            "invalid": "Age must be an integer."
        }
    )

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

student_schema = StudentSchema()    # working with a single object
students_schema = StudentSchema(many=True)  # collection
    
# No if statements. No loops. No len(). Just describing the rules.