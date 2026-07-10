from flask import Flask

from app.routes.home import home_bp
from app.routes.students import students_bp
from app.routes.auth import auth_bp
from app.error_handlers import register_error_handlers
from app.extensions import db, migrate, bcrypt
from app.models.student import Student

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
    
    return app
