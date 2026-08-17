student= {}
def add_student(name,age,roll):
    student[roll]={"name":name,"age":age}
    print("Students added successfully!")

def view_student(roll):
    if roll in student:
        print("Name: ",student[roll]["name"])
        print("Age: ",student[roll]["age"])
    else:
        print("Student not found")

def search_student(roll):
    if roll in student:
        print(f"Found : {student[roll]}")
    else:
        print("Student not found!")

def delete_student(roll):
    if roll in student:
        del student[roll]
        print("Student deleted successfully!")
    else:
        print("Student not found!")

def update_student(roll):
    if roll in student:
        student[roll]["age"] = input("Enter age: ")
        print("Student updated successfully!")
    else:
        print("Student not found!")

def menu():
    print("Welcome to Student Administration!")
    while True:

        choice = input("Enter your choice or type 'menu': ")
        if choice == "menu":
            print("1. Add Student")
            print("2. View Student")
            print("3. Search Student")
            print("4. Delete Student")
            print("5. Update Student")
            print("6. Exit")
        elif choice == "1":
            add_student(name=input("Enter name: "),age=input("Enter age: "),roll=input("Enter roll: "))
        elif choice == "2":
            view_student(roll=input("Enter roll: "))
        elif choice == "3":
            search_student(roll=input("Enter roll: "))
        elif choice == "4":
            delete_student(roll=input("Enter roll: "))
        elif choice == "5":
            update_student(roll=input("Enter roll: "))
        elif choice == "6":
            print("Thank you for using this program!")
            break
        else:
            print("Invalid choice")
menu()




