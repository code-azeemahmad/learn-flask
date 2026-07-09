from app.extensions import db

class Student(db.Model):
    __tablename__ = "student"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)

    age = db.Column(db.Integer)

    email = db.Column(db.String(120), unique=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "email": self.email
        }

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