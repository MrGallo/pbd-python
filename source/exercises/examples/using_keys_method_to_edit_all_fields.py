student = {
    "student_id": 123,
    "name": "John",
    "grade": 10,
    "average": 88.0
}

print("Please enter new values for the following:\n")
for key in student.keys():
    new_value = input(f"{key}: ")

print()
print("STUDENT INFO:\n")
for key, value in student.items():
    print(f"{key}: {value}")
