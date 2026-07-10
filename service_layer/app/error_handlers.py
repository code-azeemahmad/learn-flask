from flask import render_template, jsonify, current_app
from sqlalchemy.exc import SQLAlchemyError
from app.extensions import db
from marshmallow import ValidationError


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

'''
Error Handler? An error handler is a function that Flask automatically 
calls when a particular HTTP error occurs.

Instead of Flask's default error page: 404 Not Found
you can decide what the user sees.

@app.route("/divide")
def divide():
    return str(10 / 0)

When someone visits: /divide

Python raises: ZeroDivisionError

Flask converts that into: 500 Internal Server Error

'''