from flask import Flask, request, jsonify, Blueprint, render_template
from app.models.student import Student
from app.extensions import db

students_bp = Blueprint("student_list", __name__, url_prefix="/students")


student_list = []


@students_bp.route("/api", methods=["GET"])
def show_all_students():

    students = Student.query.all()

    student_list = []

    for student in students:
        student_list.append({
            "id": student.id,
            "name": student.name,
            "age": student.age,
            "email": student.email
        })

    return jsonify(student_list)


@students_bp.route("/<int:id>", methods=["GET"])
def get_student(id):

    student = db.session.get(Student, id)

    if student is None:
        return jsonify({
            "message": "Student not found"
        }), 404

    return jsonify({
        "id": student.id,
        "name": student.name,
        "age": student.age,
        "email": student.email
    }), 200
    

@students_bp.route("/", methods=["POST"])
def add_a_student():

    data = request.get_json()
    data = list(data.values())[0]

    student_list.append(data)

    return jsonify({
        "message": "student added successfuly",
        "username": data
    }), 201


@students_bp.route("/<int:index>", methods=["DELETE"])
def delete_student(index):

    if index < 0 or index >= len(student_list):
        return jsonify({
            "message": "No such student found"
        }), 404
    deleted_student = student_list.pop(index)

    return jsonify({
        "message": "Student deleted successfully",
        "student": deleted_student
    }), 200


@students_bp.route("/<int:index>", methods=["PUT"])
def update_a_student(index):

    if index < 0 or index >= len(student_list):
        return jsonify({
            "message": "No such student found"
        }), 404

    data = request.get_json()
    data = list(data.values())[0]
    student_list[index] = data

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
