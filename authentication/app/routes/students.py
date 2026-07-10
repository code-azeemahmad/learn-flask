from flask import request, jsonify, Blueprint, render_template
from app.models.student import Student
from app.extensions import db
from sqlalchemy.exc import SQLAlchemyError
from flask import current_app
from app.schemas.student_schema import (
    student_schema,
    students_schema
)
from app.services.student_service import StudentService
from marshmallow import ValidationError

students_bp = Blueprint("student_list", __name__, url_prefix="/students")


student_list = []


@students_bp.route("/api", methods=["GET"])
def show_all_students():

    students = Student.query.all()

    student_list = [student.to_dict() for student in students]

    return jsonify(student_list)


@students_bp.route("/<int:id>", methods=["GET"])
def get_student(id):

    student = db.session.get(Student, id)

    if student is None:
        return jsonify({
            "message": "Student not found"
        }), 404

    return jsonify(student.to_dict())
    

@students_bp.route("/", methods=["POST"])   # cleanest route (error handling, validations, normalization, SRP)
def add_student():

    data = request.get_json()

    validated_data = student_schema.load(data)

    student = StudentService.create_student(validated_data)

    return jsonify({
        "message": "Student created successfully",
        "student": student.to_dict()
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
        "student": student.to_dict()
    })



@students_bp.route("/db-test")
def db_test():
    pass
