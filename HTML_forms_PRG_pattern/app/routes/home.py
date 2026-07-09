from flask import Blueprint, request, redirect, url_for, flash
from flask import render_template


home_bp = Blueprint("home", __name__,)

@home_bp.route("/")
def home():
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
        flash("All fields are required", "error")
        return redirect(url_for("home.contact"))
    
    flash("Form submitted successfully.", "success")
    return redirect(url_for("home.home"))

'''
name=azeem ahmad
It is not JSON.
It is form data.
'''

# request.form.get returns None instead of raising an exception if the field is missing.

'''
________________________________________________________________
| Data Source      | Example            | Flask API            |
| ---------------- | ------------------ | -------------------- |
| Query parameters | `/search?q=python` | `request.args.get()` |
| HTML form        | Login form         | `request.form.get()` |
| JSON body        | React/Postman API  | `request.get_json()` |
|__________________|____________________|______________________|

'''

'''
should user stay on login?
redirect("/dashboard")  # browser automatically visits:
'''

'''
url_for() generates the URL automatically.
redirect(url_for("dashboard"))  
With url_for(), Flask finds the correct URL based on the route's endpoint.
url_for("home.home") for blueprints ("1_blueprint name. 2_function name")
'''

'''
PRG Pattern: Post → Redirect → Get
Flow:

User
  ↓
POST /register
  ↓
Save User
  ↓
Redirect
  ↓
GET /success
  ↓
Show Success Page

Notice:
The browser ends on a GET request.
Now pressing F5 simply reloads the success page—it doesn't resubmit the form.
This is a best practice you'll see in many web applications.
'''
