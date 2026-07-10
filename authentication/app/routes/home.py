from flask import Blueprint, request, redirect, url_for, flash
from flask import render_template
from flask import current_app

home_bp = Blueprint("home", __name__,)

@home_bp.route("/")
def home():
    
    current_app.logger.info("Home page is started")

    return render_template("index.html", name="azeem", age=21, university="UET, Lahore")


@home_bp.route("/about")
def about():
    return render_template("about.html")

@home_bp.route("/contact")
def contact():
    return render_template("contact.html")

@home_bp.route("/submit", methods=["POST"])
def submit():

    name = request.form.get("name")
    email = request.form.get("email")

    # validation
    if not name or not email:
        current_app.logger.info("Login failed for user")
        flash("All fields are required", "error")
        return redirect(url_for("home.contact"))
    
    current_app.logger.info("User added successfully")
    flash("Form submitted successfully.", "success")
    return redirect(url_for("home.home"))


'''
log: A log is a chronological record of events that occur in your application.

Example:

09:00:00 Application started
09:00:05 User 'Azeem' logged in
09:00:10 User requested /students
09:00:15 Database connection failed
09:00:16 Application recovered

Instead of disappearing like print() output, logs can be:

Saved to files
Sent to monitoring tools
Stored in cloud services
Searched later

Flask also has its own logger
'''
