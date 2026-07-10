from marshmallow import Schema, fields

class StudentSchema(Schema):
    # validation fields
    name = fields.String(required=True) # describing a rule


student_schema = StudentSchema()

data = {
    "name": "Azeem"
}

data = student_schema.load(data)    # validated, cleaned data