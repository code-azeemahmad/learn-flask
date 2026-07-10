from sqlalchemy.exc import SQLAlchemyError

from app.extensions import db
from app.models.student import Student
from werkzeug.exceptions import NotFound


class StudentService:

    @staticmethod
    def get_all_students():
        return Student.query.all()

    @staticmethod
    def get_student(id):

        student = db.session.get(Student, id)

        if student is None:
            raise NotFound("Student not found.")

        return student

    @staticmethod
    def create_student(data):

        student = Student(**data)

        try:
            db.session.add(student)
            db.session.commit()

            return student

        except SQLAlchemyError:
            db.session.rollback()
            raise

    @staticmethod
    def update_student(id, data):

        student = db.session.get(Student, id)

        if student is None:
            raise NotFound("Student not found.")

        student.name = data["name"]
        student.age = data["age"]
        student.email = data["email"]

        try:
            db.session.commit()

            return student

        except SQLAlchemyError:
            db.session.rollback()
            raise

    @staticmethod
    def delete_student(id):

        student = db.session.get(Student, id)

        if student is None:
            raise NotFound("Student not found.")

        try:
            db.session.delete(student)
            db.session.commit()

        except SQLAlchemyError:
            db.session.rollback()
            raise

# Repository layer for db 