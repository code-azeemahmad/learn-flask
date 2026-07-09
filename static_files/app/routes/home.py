from flask import Blueprint
from flask import render_template


home_bp = Blueprint("home", __name__,)

@home_bp.route("/")
def home():
    return render_template("index.html", name="azeem", age=21, university="UET, Lahore")

@home_bp.route("/about")
def about():
    return "hello this is about page"


# Flask automatically looks for a folder named templates/
# Jinja looks similar to Python but runs inside HTML.


