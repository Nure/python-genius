import json

with open("students.json", "r") as file:  # it opens the file and closes after the operation
    data = json.load(file)

print(data)


# Data checking
print(type(data))
print(type(data["course"]))
print(type(data["batch"]))
print(type(data["students"]))

student = data["students"][0]

print(type(student))
print(type(student["name"]))
print(type(student["age"]))
print(type(student["cgpa"]))
print(type(student["skills"]))


# Accessing nested information:
print(data["course"])

print(data["students"][0]["name"])

print(data["students"][0]["skills"])

print(data["students"][0]["address"]["city"])


# Running loop on data:
for student in data["students"]:
    print(student["name"], student["age"])



# Running extended loop on data:
for student in data["students"]:
    print(f"{student['name']} knows: ")

    for skill in student["skills"]:
        print(f"- {skill}")

# Filtering data using loop:
for student in data["students"]:
    if student["cgpa"] > 3.7:
        print(student["name"])


# Find for a skill and find all students who know that skill.
skill_to_find = input("Enter a skill: ").lower()

for student in data["students"]:
    for skill in student["skills"]:
        if skill_to_find == skill.lower():
            print(student["name"])
        else:
            print("No students at bongoDev has the target skill")