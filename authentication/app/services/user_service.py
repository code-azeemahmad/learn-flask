from sqlalchemy.exc import SQLAlchemyError
from werkzeug.exceptions import Conflict

from app.extensions import db, bcrypt
from app.models.user import User


class UserService:

    @staticmethod
    def register(data):

        existing_user = User.query.filter_by(
            email=data["email"]
        ).first()

        if existing_user:
            raise Conflict("Email is already registered.")

        password_hash = bcrypt.generate_password_hash(
            data["password"]
        ).decode("utf-8")

        user = User(
            email=data["email"],
            password_hash=password_hash,
            role="student"
        )

        try:
            db.session.add(user)
            db.session.commit()

            return user

        except SQLAlchemyError:
            db.session.rollback()
            raise