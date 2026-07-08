from flask import Blueprint, jsonify, request

books_bp = Blueprint("books", __name__, url_prefix="/books")

books = [
    "Python Crash Course",
    "Clean Code",
    "Fluent Python"
]

# GET /books
@books_bp.route("/", methods=["GET"])
def get_all_books():
    return jsonify({
        "books": books
    })


# GET /books/0
@books_bp.route("/<int:index>", methods=["GET"])
def get_book(index):

    if index < 0 or index >= len(books):
        return jsonify({
            "error": "Book not found"
        }), 404

    return jsonify({
        "book": books[index]
    })


# POST /books
@books_bp.route("/", methods=["POST"])
def add_book():

    data = request.get_json()
    book = data.get("title")

    if not book:
        return jsonify({
            "error": "Book title is required"
        }), 400

    books.append(book)

    return jsonify({
        "message": "Book added successfully",
        "book": book
    }), 201


# PUT /books/1
@books_bp.route("/<int:index>", methods=["PUT"])
def update_book(index):

    if index < 0 or index >= len(books):
        return jsonify({
            "error": "Book not found"
        }), 404

    data = request.get_json()
    book = data.get("title")

    if not book:
        return jsonify({
            "error": "Book title is required"
        }), 400

    books[index] = book

    return jsonify({
        "message": "Book updated successfully",
        "book": book
    })


# DELETE /books/1
@books_bp.route("/<int:index>", methods=["DELETE"])
def delete_book(index):

    if index < 0 or index >= len(books):
        return jsonify({
            "error": "Book not found"
        }), 404

    deleted_book = books.pop(index)

    return jsonify({
        "message": "Book deleted successfully",
        "book": deleted_book
    })