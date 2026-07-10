from app.extensions import db
from flask_login import UserMixin


class User(UserMixin, db.Model):
    # UserMixin simply provides these default implementations for you.
    '''get_id(), is_authenticated, is_active, is_anonymous'''

    __tablename__ = "users"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    email = db.Column(
        db.String(255),
        unique=True,
        nullable=False
    )

    password_hash = db.Column(
        db.String(255),
        nullable=False
    )

    role = db.Column(
        db.String(20),
        nullable=False,
        default="student"
    )

    student = db.relationship(
        "Student",
        back_populates="user",
        uselist=False
    )

'''
User
-----
id
email
password_hash
role
        │
        │ One-to-One
        ▼
Student
--------
id
name
age
'''

'''
This is a common design when authentication data and domain data have different responsibilities.

User → Authentication & Authorization
- email
- password_hash
- role

Student → Business/Application data
- name
- age
- courses
-GPA
Keeping them separate follows the Single Responsibility Principle and makes it easier to support multiple user types later (e.g., teachers, admins).
'''