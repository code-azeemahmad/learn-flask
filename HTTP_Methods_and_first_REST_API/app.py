from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, User!"

students = ["azeem", "bilal", "ahmad"]

# Earlier we didn't write this. That's because Flask assumes: GET by default.
@app.route("/students", methods=["GET"])
def show_all_students():

    return jsonify(students)


@app.route("/students/<int:index>", methods=["GET"])
def get_student(index):
    if index >= len(students):
        return jsonify({
            "message": "No such student found"
        }), 404
    else:
        return jsonify({
            "username": students[index]
        }), 200
    

@app.route("/students", methods=["POST"])
def add_a_student():

    data = request.get_json()   # converts that JSON into a Python dictionary.
    data = list(data.values())[0]   # converts that dictionary into a list and gets the first value.

    students.append(data)

    return jsonify({
        "message": "student added successfuly",
        "username": data
    }), 201


@app.route("/students/<int:index>", methods=["DELETE"])
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


@app.route("/students/<int:index>", methods=["PUT"])
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


if __name__ == "__main__":
    app.run(debug=True)



'''
The route has no dynamic parameters, so Flask calls: @app.route("/students")
def show_all_students(students):
But your function expects one argument, which causes the error. show_all_students()
'''

# REST stands for: Representational State Transfer
# Think of REST as a set of rules for designing APIs.

# JSON is text while a Python dictionary is an in-memory object.