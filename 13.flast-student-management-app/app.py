from flask import Flask, jsonify, redirect, render_template, request, url_for

from database import init_db
from models.student import Student, StudentRepository

app = Flask(__name__)

# Create the database/table automatically when the app starts.
init_db()


@app.route("/")
def index():
    """Show the frontend form and all saved students."""
    students = StudentRepository.get_all()
    return render_template("index.html", students=students)


@app.route("/students", methods=["POST"])
def create_student():
    """Create a Student object from frontend form data and save it."""
    student = Student(
        name=request.form["name"],
        age=int(request.form["age"]),
        email=request.form["email"],
        cgpa=float(request.form["cgpa"]),
        course=request.form["course"],
        skills=request.form["skills"],
    )

    StudentRepository.create(student)
    return redirect(url_for("index"))


@app.route("/students/<int:student_id>/edit", methods=["GET"])
def edit_student_page(student_id):
    """Show the edit form for one student."""
    student = StudentRepository.get_by_id(student_id)

    if student is None:
        return "Student not found", 404

    return render_template("edit.html", student=student)


@app.route("/students/<int:student_id>/edit", methods=["POST"])
def update_student(student_id):
    """Update an existing student."""
    student = Student(
        student_id=student_id,
        name=request.form["name"],
        age=int(request.form["age"]),
        email=request.form["email"],
        cgpa=float(request.form["cgpa"]),
        course=request.form["course"],
        skills=request.form["skills"],
    )

    StudentRepository.update(student)
    return redirect(url_for("index"))


@app.route("/students/<int:student_id>/delete", methods=["POST"])
def delete_student(student_id):
    """Delete a student."""
    StudentRepository.delete(student_id)
    return redirect(url_for("index"))


# -------------------------
# REST API endpoints
# -------------------------

@app.route("/api/students", methods=["GET"])
def api_get_students():
    students = StudentRepository.get_all()
    return jsonify([student.to_dict() for student in students])


@app.route("/api/students/<int:student_id>", methods=["GET"])
def api_get_student(student_id):
    student = StudentRepository.get_by_id(student_id)

    if student is None:
        return jsonify({"error": "Student not found"}), 404

    return jsonify(student.to_dict())


@app.route("/api/students", methods=["POST"])
def api_create_student():
    data = request.get_json()

    required_fields = ["name", "age", "email", "cgpa", "course", "skills"]

    if not data or not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required student information"}), 400

    student = Student(
        name=data["name"],
        age=int(data["age"]),
        email=data["email"],
        cgpa=float(data["cgpa"]),
        course=data["course"],
        skills=data["skills"],
    )

    student_id = StudentRepository.create(student)
    student.student_id = student_id

    return jsonify(student.to_dict()), 201


if __name__ == "__main__":
    app.run(debug=True)
