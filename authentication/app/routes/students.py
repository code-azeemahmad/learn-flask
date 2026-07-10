from flask import Blueprint, jsonify, request

from app.schemas.student_schema import (
    student_schema,
    students_schema
)
from app.services.student_service import StudentService


students_bp = Blueprint(
    "student_list",
    __name__,
    url_prefix="/students"
)


@students_bp.route("/", methods=["GET"])
def show_all_students():

    students = StudentService.get_all_students()

    return jsonify(students_schema.dump(students))


@students_bp.route("/<int:id>", methods=["GET"])
def get_student(id):

    student = StudentService.get_student(id)

    return jsonify(student_schema.dump(student))


@students_bp.route("/", methods=["POST"])
def add_student():

    data = request.get_json()

    validated_data = student_schema.load(data)

    student = StudentService.create_student(validated_data)

    return jsonify({
        "message": "Student created successfully",
        "student": student_schema.dump(student)
    }), 201


@students_bp.route("/<int:id>", methods=["PUT"])
def update_student(id):

    data = request.get_json()

    validated_data = student_schema.load(data)

    student = StudentService.update_student(id, validated_data)

    return jsonify({
        "message": "Student updated successfully",
        "student": student_schema.dump(student)
    })


@students_bp.route("/<int:id>", methods=["DELETE"])
def delete_student(id):

    StudentService.delete_student(id)

    return jsonify({
        "message": "Student deleted successfully"
    }), 200