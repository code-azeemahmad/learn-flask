from flask import render_template, jsonify, current_app
from sqlalchemy.exc import SQLAlchemyError
from app.extensions import db
from marshmallow import ValidationError
from werkzeug.exceptions import NotFound


def register_error_handlers(app):

    @app.errorhandler(404)
    def not_found(error):
        current_app.logger.info("404 - Page not found")
        return render_template("404.html"), 404

    @app.errorhandler(500)
    def internal_error(error):
        current_app.logger.exception("Unexpected exception")
        return render_template("500.html"), 500

    @app.errorhandler(SQLAlchemyError)
    def handle_database_error(error):
        current_app.logger.exception("Database error")  # create_student service is responsible for rollback

        return jsonify({
            "message": "A database error occurred."
        }), 500
    
    @app.errorhandler(ValidationError)
    def handle_validation_error(error):
        return jsonify({
            "errors": error.messages
        }), 400

    @app.errorhandler(NotFound)
    def handle_not_found(error):

        return jsonify({
            "message": error.description
        }), 404
    
'''
Now every service can simply: raise NotFound("Student not found.")

instead of every route repeating:

if student is None:
    return jsonify({
        "message": "Student not found"
    }), 404
'''