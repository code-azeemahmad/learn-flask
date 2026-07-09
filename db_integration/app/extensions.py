from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
# login_manager = LoginManager()

'''
Flask-Migrate works with SQLAlchemy to:
- Detect model changes
- Generate migration files
- Apply them to the database
It uses another library called Alembic behind the scenes.
'''

# flask --app run.py db init    run once
# flask --app run.py db migrate -m "Create student table"
# flask --app run.py db upgrade


'''
alembic_version table?
It's an internal table used by Alembic to remember:
"Which migrations have already been applied to this database?"
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