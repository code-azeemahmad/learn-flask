from flask import Flask

from app.routes.home import home_bp
from app.routes.students  import students_bp

def create_app():   # Application Factory Pattern

    # Instead of having one fixed app object, we have a factory that can create one whenever it's needed.

    app = Flask(__name__)

    app.config.from_object("app.config.Config")

    app.register_blueprint(home_bp)
    app.register_blueprint(students_bp)
    
    return app