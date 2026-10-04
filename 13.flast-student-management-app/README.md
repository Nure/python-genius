# Flask Student Management System

A beginner-friendly Flask project for learning:

- Python classes and objects
- Strings, integers, floats, lists, and dictionaries
- HTML forms
- Flask routes
- REST APIs
- JSON
- CRUD operations
- SQLite using Python's built-in `sqlite3` module

## Architecture

```text
Browser / Frontend
        |
        v
Flask Route
        |
        v
Student Class / Object
        |
        v
StudentRepository
        |
        v
SQLite Database
```

## Features

- Add a student from the browser
- View all students
- Edit a student
- Delete a student
- Store information permanently in SQLite
- View all students as JSON
- Fetch an individual student through the API
- Create a student through a JSON API

## Student Information

Each student has:

- ID
- Name
- Age
- Email
- CGPA
- Course
- Skills

## Why SQLite?

SQLite is perfect for this classroom project because Python includes the
`sqlite3` module by default.

You do **not** need to install MySQL, PostgreSQL, or a database server.

The file:

```text
students.db
```

will be created automatically when the Flask application starts.

---

# 1. Create a Virtual Environment

## macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

## Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

# 2. Install Flask

```bash
pip install -r requirements.txt
```

---

# 3. Start the Application

```bash
python app.py
```

You should see something similar to:

```text
Running on http://127.0.0.1:5000
```

Open:

```text
http://127.0.0.1:5000
```

in your browser.

---

# 4. Frontend Flow

The user enters student information in the browser:

```text
Name
Age
Email
CGPA
Course
Skills
```

The HTML form sends the data to:

```text
POST /students
```

Flask receives the values using:

```python
request.form
```

Then Flask creates a Student object:

```python
student = Student(
    name=request.form["name"],
    age=int(request.form["age"]),
    email=request.form["email"],
    cgpa=float(request.form["cgpa"]),
    course=request.form["course"],
    skills=request.form["skills"]
)
```

That is an important OOP lesson.

The `Student` class is the blueprint.

```python
class Student:
```

This:

```python
student = Student(...)
```

creates an object from the class.

---

# 5. Database

The application uses:

```python
import sqlite3
```

The database table is created automatically:

```sql
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    email TEXT NOT NULL,
    cgpa REAL NOT NULL,
    course TEXT NOT NULL,
    skills TEXT NOT NULL
)
```

Notice the relationship between Python and database data types:

| Python | SQLite |
|---|---|
| `str` | `TEXT` |
| `int` | `INTEGER` |
| `float` | `REAL` |

---

# 6. REST API

## Get All Students

```http
GET /api/students
```

Open in browser:

```text
http://127.0.0.1:5000/api/students
```

Example response:

```json
[
  {
    "id": 1,
    "name": "Rahim Ahmed",
    "age": 24,
    "email": "rahim@example.com",
    "cgpa": 3.75,
    "course": "DevOps & Cloud Engineering",
    "skills": "Python, Linux, Docker"
  }
]
```

This teaches:

```text
Student Object
      |
      v
to_dict()
      |
      v
Python Dictionary
      |
      v
jsonify()
      |
      v
JSON
```

---

## Get One Student

```http
GET /api/students/1
```

Example:

```text
http://127.0.0.1:5000/api/students/1
```

---

## Create Student Through API

```http
POST /api/students
Content-Type: application/json
```

Example body:

```json
{
  "name": "Ayesha Khan",
  "age": 22,
  "email": "ayesha@example.com",
  "cgpa": 3.9,
  "course": "DevOps & Cloud Engineering",
  "skills": "Python, AWS, Terraform"
}
```

You can test this using Postman or curl.

Example curl:

```bash
curl -X POST http://127.0.0.1:5000/api/students \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Ayesha Khan",
    "age": 22,
    "email": "ayesha@example.com",
    "cgpa": 3.9,
    "course": "DevOps & Cloud Engineering",
    "skills": "Python, AWS, Terraform"
  }'
```

---

# 7. Project Structure

```text
flask_student_management/
|
|-- app.py
|-- database.py
|-- requirements.txt
|-- README.md
|
|-- models/
|   |-- __init__.py
|   `-- student.py
|
|-- templates/
|   |-- index.html
|   `-- edit.html
|
`-- static/
    `-- style.css
```

---

# 8. Important Files

## `app.py`

Contains Flask routes.

Examples:

```python
@app.route("/")
```

```python
@app.route("/students", methods=["POST"])
```

```python
@app.route("/api/students", methods=["GET"])
```

This is the application/controller layer.

---

## `models/student.py`

Contains:

```python
class Student
```

and:

```python
class StudentRepository
```

The `Student` class represents student data.

The `StudentRepository` class handles database operations.

---

## `database.py`

Creates and connects to SQLite.

---

# 9. CRUD

CRUD means:

```text
C = Create
R = Read
U = Update
D = Delete
```

This project demonstrates all four:

```text
Create -> Add Student
Read   -> Student List
Update -> Edit Student
Delete -> Delete Student
```

---

# 10. Classroom Explanation

A useful way to explain the application is:

```text
USER
 |
 | fills HTML form
 v
FRONTEND
 |
 | HTTP POST
 v
FLASK
 |
 | creates
 v
STUDENT OBJECT
 |
 | passes object to
 v
REPOSITORY
 |
 | executes SQL
 v
SQLITE DATABASE
```

When displaying information:

```text
SQLITE
 |
 v
DATABASE ROW
 |
 v
STUDENT OBJECT
 |
 v
HTML PAGE
```

For the REST API:

```text
SQLITE
 |
 v
STUDENT OBJECT
 |
 v
to_dict()
 |
 v
DICTIONARY
 |
 v
JSON
```

---

# Suggested Student Exercises

## Exercise 1

Add a new field:

```text
phone
```

Update:

- Student class
- Database table
- HTML form
- API output

## Exercise 2

Add:

```text
department
```

## Exercise 3

Create a search feature.

The user enters a student name and the application shows matching students.

## Exercise 4

Create this endpoint:

```http
GET /api/students/cgpa/3.5
```

Return students whose CGPA is greater than or equal to `3.5`.

## Exercise 5

Create:

```http
DELETE /api/students/<id>
```

## Exercise 6

Instead of storing skills as:

```text
Python, Linux, Docker
```

convert them into a Python list:

```python
["Python", "Linux", "Docker"]
```

and return a JSON array from the API.

---

# Learning Objective

Students should be able to explain this complete flow:

```text
HTML form
    ↓
HTTP request
    ↓
Flask route
    ↓
Python dictionary
    ↓
Student class
    ↓
Student object
    ↓
SQLite
    ↓
Student object
    ↓
Dictionary
    ↓
JSON / HTML
```

That is the main purpose of the project.
