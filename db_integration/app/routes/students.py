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
def add_student():

    data = request.get_json()

    student = Student(
        name=data["name"],
        age=data["age"],
        email=data["email"]
    )

    db.session.add(student)

    db.session.commit()

    return jsonify({
        "message": "Student created successfully",
        "student": {
            "id": student.id,
            "name": student.name,
            "age": student.age,
            "email": student.email
        }
    }), 201


@students_bp.route("/<int:id>", methods=["DELETE"])
def delete_student(id):

    student = db.session.get(Student, id)

    if student is None:
        return jsonify({
            "message": "Student not found"
        }), 404

    db.session.delete(student)

    db.session.commit()

    return jsonify({
        "message": "Student deleted successfully"
    }), 200


@students_bp.route("/<int:id>", methods=["PUT"])
def update_student(id):

    student = db.session.get(Student, id)
    if student is None:
        return jsonify({
            "message": "Student not found"
        }), 404

    data = request.get_json()
    student.name = data["name"]
    student.age = data["age"]
    student.email = data["email"]

    db.session.commit()

    return jsonify({
        "message": "Student updated successfully",
        "student": {
            "id": student.id,
            "name": student.name,
            "age": student.age,
            "email": student.email
        }
    }), 200



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
