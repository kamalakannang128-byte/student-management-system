# Student Management System - By Kamalakannan G
students = []

def add_student():
    name = input("Enter Name: ")
    mark = input("Enter Mark: ")
    students.append({"name": name, "mark": mark})
    print("Student Added Successfully!")

def view_students():
    if not students:
        print("No students yet!")
    else:
        for s in students:
            print(f"Name: {s['name']}, Mark: {s['mark']}")

while True:
    print("\n--- Student Menu ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")
    ch = input("Enter Choice: ")
    if ch == '1':
        add_student()
    elif ch == '2':
        view_students()
    elif ch == '3':
        print("Bye!")
        break
    else:
        print("Wrong choice!")
