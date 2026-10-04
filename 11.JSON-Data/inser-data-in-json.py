import json


# 1. Create the Student class
class Student:
    def __init__(self, name, age, cgpa, skills):
        self.name = name
        self.age = age
        self.cgpa = cgpa
        self.skills = skills

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"CGPA: {self.cgpa}")
        print(f"Skills: {', '.join(self.skills)}")
        print("-" * 30)


# 2. Read existing student data from JSON file
with open("students.json", "r") as file:
    data = json.load(file)


# 3. Create a new student as a dictionary
new_student = {
    "id": 111,
    "name": "Roman",
    "age": 23,
    "cgpa": 3.9,
    "skills": ["Python", "Docker"],
    "address": {
        "city": "Dhaka",
        "country": "Bangladesh"
    }
}


# 4. Add the new student to the students list
data["students"].append(new_student)


# 5. Save the updated data back to the JSON file
with open("students.json", "w") as file:
    json.dump(data, file, indent=4)


# 6. Create an empty list for Student objects
students = []


# 7. Convert each dictionary into a Student object
for item in data["students"]:
    student = Student(
        item["name"],
        item["age"],
        item["cgpa"],
        item["skills"]
    )

    students.append(student)


# 8. Display all Student objects
for student in students:
    student.display()