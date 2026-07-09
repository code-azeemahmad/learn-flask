from flask import render_template
from flask import current_app

def register_error_handlers(app):

    @app.errorhandler(404)  # if a user visits this route /bookssss
    def not_found(error):
        current_app.logger.info("Unexpected exception")
        return render_template("404.html"), 404

    @app.errorhandler(500)  # /divide
    def internal_error(error):
        current_app.logger.info("Unexpected exception")
        return render_template("500.html"), 500


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