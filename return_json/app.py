from flask import Flask, jsonify # type: ignore

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, User"

@app.route('/user')
def user():
    return jsonify({    # Flask automatically converts dictionaries to JSON.
        "name": "azeem",
        "age": 21,
        "course": "flask"
    })

@app.route("/success")
def success():

    return "Everything is OK", 200

@app.route("/notfound")
def not_found():

    return "Page not found", 404

@app.route("/error")
def error():

    return "Something went wrong!", 500

if __name__ == "__main__":
    app.run(debug=True)