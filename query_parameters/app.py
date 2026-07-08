from flask import Flask, request # type: ignore


app = Flask(__name__)

# Query parameters
@app.route("/")
def home():
    return "hello"

@app.route("/search")
def search():
    query = request.args.get("q")   # Think of it like a dictionary:
    return f"You searched for {query}"

@app.route("/findpage")
def find_page():
    query = request.args.get("q")
    page = request.args.get("page", default=1, type=int)
    return f"You searched for {query} and {page}"

if __name__ == "__main__":
    app.run(debug = True)

'''
Dynamic routes are part of the URL. Query parameters come after a ?.
Everything after that is optional information.

Example: Google
                https://www.google.com/search?q=flask

The search term is a query parameter.
'''

# .venv\Scripts\activate.bat