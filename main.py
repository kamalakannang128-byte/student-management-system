import json
import os

FILE_NAME = "students_by_kamalesh.json"
students = []

def load_data():
    global students
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as f:
                students = json.load(f)
            print(f"Loaded {len(students)} students from file!")
        except:
            students = []

def save_data():
    with open(FILE_NAME, "w") as f:
        json.dump(students, f, indent=2)
    print("Data saved!")

def add_student():
    name = input("Enter Name: ").strip()
    if not name:
        print("Name cannot be empty!")
        return
    try:
        mark = int(input("Enter Mark (0-100): "))
        if not 0 <= mark <= 100:
            print("Mark should be 0-100!")
            return
    except ValueError:
        print("Please enter valid number!")
        return
    
    students.append({"name": name, "mark": mark})
    save_data()
    print(f"Student {name} Added Successfully!")

def view_students():
    if not students:
        print("No students yet!")
        return
    print("\n--- All Students ---")
    for i, s in enumerate(students, 1):
        print(f"{i}. Name: {s['name']}, Mark: {s['mark']}")

def search_student():
    if not students:
        print("No students yet!")
        return
    search_name = input("Enter name to search: ").strip().lower()
    found = [s for s in students if search_name in s['name'].lower()]
    if found:
        print(f"Found {len(found)} student(s):")
        for s in found:
            print(f"Name: {s['name']}, Mark: {s['rk']}")
    else:
        print("No student found with that name!")

def delete_student():
    view_students()
    if not students:
        return
    try:
        idx = int(input("Enter student number to delete: ")) - 1
        if 0 <= idx < len(students):
            removed = students.pop(idx)
            save_data()
            print(f"Deleted {removed['name']}!")
        else:
            print("Invalid number!")
    except ValueError:
        print("Enter valid number!")

load_data()
while True:
    print("\n--- Student Menu ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")
    ch = input("Enter Choice: ").strip()
    
    if ch == '1':
        add_student()
    elif ch == '2':
        view_students()
    elif ch == '3':
        search_student()
    elif ch == '4':
        delete_student()
    elif ch == '5':
        print("Bye! Data saved in students.json")
        break
    else:
        print("Wrong choice! Enter 1-5")
