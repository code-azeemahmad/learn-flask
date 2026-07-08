from flask import Flask # type: ignore

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, flask!"

@app.route("/about")
def about():
    return "Hey! This is Azeem Ahmad here"

@app.route("/contact")
def contact():
    return "azeemahmadd9@gmail.com"

if __name__ == "__main__":
    app.run(debug = True)


'''
WSGI stands for: (Web Server Gateway Interface)
It's a standard that defines how a web server communicates with a Python web application.
'''