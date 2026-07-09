'''
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
'''

'''
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
'''

'''
__init__.py
Later, in create_app():

from app.extensions import db

def create_app():
    app = Flask(__name__)
    db.init_app(app)
    return app
'''

'''
| Extension          | Purpose                                     | When you'll use it                   |
| ------------------ | ------------------------------------------- | ------------------------------------ |
| Flask-SQLAlchemy   | Database ORM                                | Almost every database-backed app     |
| Flask-Migrate      | Database migrations                         | When your database schema changes    |
| Flask-Login        | User login with sessions                    | Traditional web apps                 |
| Flask-JWT-Extended | JWT authentication                          | REST APIs, React, mobile apps        |
| Flask-Mail         | Send emails                                 | Password resets, verification emails |
| Flask-CORS         | Allow frontend requests from another domain | React/Vue/Angular frontend           |

'''