from flask import request, jsonify, Blueprint, render_template
from app.models.student import Student
from app.extensions import db
from sqlalchemy.exc import SQLAlchemyError
from flask import current_app
from app.validators.student_validator import StudentValidator

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
    

@students_bp.route("/", methods=["POST"])
def add_student():

    data = request.get_json()

    errors = StudentValidator.validate(data)

    if errors:
        return jsonify({"errors": errors}), 400
    
    student = Student(
        name=data["name"],
        age=data["age"],
        email=data["email"]
    )
    
    try:
        db.session.add(student)
        db.session.commit()

        return jsonify({
            "message": "Student created successfully",
            "student": student.to_dict()
        }), 201

    except SQLAlchemyError:
        db.session.rollback()
        current_app.logger.exception("Failed to create student")

        return jsonify({
            "message": "Failed to create student"
        }), 500


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

'''
A Student object already knows everything about itself.
return jsonify({
    "message": "Updated",
    "student": {
        "id": student.id,
        "name": student.name,
        "age": student.age,
        "email": student.email
    }
})
The highlighted dictionary is repeated everywhere.
Solution: return jsonify(student.to_dict())
'''


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
