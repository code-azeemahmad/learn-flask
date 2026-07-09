from flask import Flask, request, jsonify, Blueprint, render_template


students_bp = Blueprint("students", __name__, url_prefix="/students")

students = [
"Ali",
"Azeem",
"Ahmed",
"John"
]

@students_bp.route("/")
def home_students():
    return render_template(
    "students.html",
    students=students
)


@students_bp.route("/api", methods=["GET"])
def show_all_students():

    return jsonify(students)


@students_bp.route("/<int:index>", methods=["GET"])
def get_student(index):
    if index >= len(students):
        return jsonify({
            "message": "No such student found"
        }), 404
    else:
        return jsonify({
            "username": students[index]
        }), 200
    

@students_bp.route("/", methods=["POST"])
def add_a_student():

    data = request.get_json()   # converts that JSON into a Python dictionary.
    data = list(data.values())[0]   # converts that dictionary into a list and gets the first value.

    students.append(data)

    return jsonify({
        "message": "student added successfuly",
        "username": data
    }), 201


@students_bp.route("/<int:index>", methods=["DELETE"])
def delete_student(index):

    if index < 0 or index >= len(students):
        return jsonify({
            "message": "No such student found"
        }), 404
    deleted_student = students.pop(index)

    return jsonify({
        "message": "Student deleted successfully",
        "student": deleted_student
    }), 200


@students_bp.route("/<int:index>", methods=["PUT"])
def update_a_student(index):

    if index < 0 or index >= len(students):
        return jsonify({
            "message": "No such student found"
        }), 404

    data = request.get_json()
    data = list(data.values())[0]
    students[index] = data

    return jsonify({
        "message": "student updated successfuly",
        "username": data
    }), 201

@students_bp.route("/db-test")
def db_test():
    pass


''' ORM lifecycle
Python Object
      │
      ▼
db.session.add()
      │
      ▼
db.session.commit()
      │
      ▼
Database Row
'''
''' Query lifecycle
Database Row
      │
      ▼
Student.query
      │
      ▼
Python Object
'''
