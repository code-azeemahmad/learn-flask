from flask import Flask # type: ignore

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, flask!"

# Dynamic routing
@app.route("/about/<username>")
def about(username):
    return f"Welcome! This is {username} here"

# Multiple variables
@app.route("/student/<username>/<course>/")
def student(username, course):
    return f"{username} is enrolled in {course}"

# Type convertors
@app.route("/square/<int:number>")
def square(number):
    return str(number * number)

'''
Because Flask expects the view function to return a valid HTTP response.
    A simple response can be:
1) a string
2) HTML
3) JSON (using jsonify)
4) a Response object
    But not a plain integer.
'''

if __name__ == "__main__":
    app.run(debug = True)


'''
WSGI stands for: (Web Server Gateway Interface)
It's a standard that defines how a web server communicates with a Python web application.
'''