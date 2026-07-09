from app.extensions import db

class Student(db.Model):    # "This isn't just a normal Python class. It represents a database table."

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100))

    age = db.Column(db.Integer)

    email = db.Column(db.String(120))


''' Object Relational Mapping
student = Student(
    name="Azeem",
    age=21,
    email="azeem@example.com"
)
represents a single row in the students table.
'''

'''
A migration is a set of instructions that changes the database schema.
database migrations, SQLAlchemy generate the 
actual table in your PostgreSQL database.
'''