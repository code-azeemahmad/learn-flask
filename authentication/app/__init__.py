from flask import Flask

from app.routes.home import home_bp
from app.routes.students import students_bp
from app.routes.auth import auth_bp
from app.error_handlers import register_error_handlers
from app.models.student import Student
from app.extensions import (
    db,
    migrate,
    bcrypt,
    login_manager
)

def create_app():

    app = Flask(__name__)

    app.config.from_object("app.config.Config")

    db.init_app(app)
    migrate.init_app(app, db)
    

    app.register_blueprint(home_bp)
    app.register_blueprint(students_bp)
    app.register_blueprint(auth_bp)

    register_error_handlers(app)

    bcrypt.init_app(app)
    login_manager.init_app(app)

    import app.login_manager    # importing a module we never use

    login_manager.login_view = "auth.login"
    login_manager.login_message = "Please log in to access this page."
    login_manager.login_message_category = "warning"
    
    return app
