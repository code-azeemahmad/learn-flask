from flask import Blueprint

home_bp = Blueprint("home", __name__)

@home_bp.route("/")
def home():
    return "Welcome home"

@home_bp.route("/about")
def about():
    return "hello this is about page"