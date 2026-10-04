from database import get_connection


class Student:
    """
    Student is the model class.

    Every Student(...) we create is an OBJECT made from this CLASS.
    """

    def __init__(
        self,
        name,
        age,
        email,
        cgpa,
        course,
        skills,
        student_id=None,
    ):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.email = email
        self.cgpa = cgpa
        self.course = course
        self.skills = skills

    def to_dict(self):
        """Convert the Student object into a Python dictionary."""
        return {
            "id": self.student_id,
            "name": self.name,
            "age": self.age,
            "email": self.email,
            "cgpa": self.cgpa,
            "course": self.course,
            "skills": self.skills,
        }


class StudentRepository:
    """
    This class contains database operations.

    Keeping database code here helps students see separation of concerns:
    Flask routes -> Student objects -> Repository -> SQLite database
    """

    # Use @staticmethod when a function logically belongs inside a class, but it does not need to access any object-specific (self) data.
    @staticmethod
    def create(student):
        connection = get_connection()

        cursor = connection.execute(
            """
            INSERT INTO students (name, age, email, cgpa, course, skills)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                student.name,
                student.age,
                student.email,
                student.cgpa,
                student.course,
                student.skills,
            ),
        )

        connection.commit()
        student_id = cursor.lastrowid
        connection.close()

        return student_id

    @staticmethod
    def get_all():
        connection = get_connection()

        rows = connection.execute(
            "SELECT * FROM students ORDER BY id DESC"
        ).fetchall()

        connection.close()

        students = []

        for row in rows:
            student = Student(
                student_id=row["id"],
                name=row["name"],
                age=row["age"],
                email=row["email"],
                cgpa=row["cgpa"],
                course=row["course"],
                skills=row["skills"],
            )

            students.append(student)

        return students

    @staticmethod
    def get_by_id(student_id):
        connection = get_connection()

        row = connection.execute(
            "SELECT * FROM students WHERE id = ?",
            (student_id,),
        ).fetchone()

        connection.close()

        if row is None:
            return None

        return Student(
            student_id=row["id"],
            name=row["name"],
            age=row["age"],
            email=row["email"],
            cgpa=row["cgpa"],
            course=row["course"],
            skills=row["skills"],
        )

    @staticmethod
    def update(student):
        connection = get_connection()

        connection.execute(
            """
            UPDATE students
            SET name = ?, age = ?, email = ?, cgpa = ?, course = ?, skills = ?
            WHERE id = ?
            """,
            (
                student.name,
                student.age,
                student.email,
                student.cgpa,
                student.course,
                student.skills,
                student.student_id,
            ),
        )

        connection.commit()
        connection.close()

    @staticmethod
    def delete(student_id):
        connection = get_connection()

        connection.execute(
            "DELETE FROM students WHERE id = ?",
            (student_id,),
        )

        connection.commit()
        connection.close()
