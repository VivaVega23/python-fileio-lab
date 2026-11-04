from pathlib import Path
FILE_PATH = Path("students.txt")
def add_student(name, course):
    with open(FILE_PATH, "a", encoding="utf-8") as file:
        file.write(f"{name},{course}\n")
    print("Student added successfully!")
def view_students():
    try:
        with open(FILE_PATH, "r", encoding="utf-8") as file:
            print("\nStudent Records:")
            for line in file:
                name, course = line.strip().split(",", 1)
                print(f"Name: {name}, Course: {course}")
    except FileNotFoundError:
     print("No student records found.")

def count_students():
    try:
        with open(FILE_PATH, "r", encoding="utf-8") as file:
            return len(file.readlines())
    except FileNotFoundError:
        return 0
add_student("John", "Python")
add_student("Emma", "Database")

view_students()
print("\nTotal Students:", count_students())