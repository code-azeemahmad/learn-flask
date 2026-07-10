from flask import Flask

from app.routes.home import home_bp
from app.routes.students import students_bp
from app.error_handlers import register_error_handlers
from app.extensions import db, migrate
from app.models.student import Student  # No attendance → no migration

def create_app():

    app = Flask(__name__)

    app.config.from_object("app.config.Config")

    db.init_app(app)
    migrate.init_app(app, db)
    

    app.register_blueprint(home_bp)
    app.register_blueprint(students_bp)

    register_error_handlers(app)
    
    return app


''' testing
(.venv) C:\Drives\F_Projects\flask\learn-flask\db_integration>python run.py
✅ Connected to PostgreSQL!
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
'''