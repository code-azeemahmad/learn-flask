from app.extensions import login_manager
from app.models.user import User
from app.extensions import db

'''Flask-Login calls it automatically whenever it needs to 
restore the logged-in user from the session.'''
@login_manager.user_loader
def load_user(user_id):
    """
    Load a user from the database using the user ID
    stored in the session.
    """

    return db.session.get(User, int(user_id))