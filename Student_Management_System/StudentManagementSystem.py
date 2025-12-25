students = []

def add_student():
    roll = int(input("Enter roll: "))
    name = input("Enter name: ")
    marks = int(input("Enter marks: "))
    students.append({"roll": roll, "name": name, "marks": marks})

def view_students():
    for s in students:
        print(s)

def search_student():
    roll = int(input("Enter roll to search: "))
    for s in students:
        if s["roll"] == roll:
            print(s)
            return
    print("Student not found")

while True:
    print("\n1.Add  2.View  3.Search  4.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        break
    else:
        print("Invalid choice")
