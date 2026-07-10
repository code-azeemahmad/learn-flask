from app.extensions import db
from app.models.student import Student
from sqlalchemy.exc import SQLAlchemyError


class StudentService:

    @staticmethod
    def create_student(data):
        """
        Create a new student and save it to the database.

        Args:
            data (dict): Validated student data.

        Returns:
            Student: The newly created student.
        """

        student = Student(**data)

        try:
            db.session.add(student)
            db.session.commit()
            return student
    
        # The service knows exactly what transaction needs rolling back. The error handler doesn't.
        # let every service be responsible for its own rollback.

        except SQLAlchemyError:
            db.session.rollback()
            raise
