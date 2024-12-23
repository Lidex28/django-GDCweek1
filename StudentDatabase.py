def add_student(database):
    name = input("Enter student's name: ").strip()
    if name in database:
        print(f"A student named '{name}' already exists.")
    else:
        age = input("Enter student's age: ").strip()
        grade = input("Enter student's grade: ").strip()
        additional_info = input("Enter any additional details (optional): ").strip()
        database[name] = {
            "age": age,
            "grade": grade,
            "additional_info": additional_info
        }
        print(f"Student '{name}' has been added.")

def view_student(database):
    name = input("Enter the name of the student to view: ").strip()
    if name in database:
        print(f"\nDetails for '{name}':")
        for key, value in database[name].items():
            print(f"{key.capitalize()}: {value}")
    else:
        print(f"No student found with the name '{name}'.")

def list_all_students(database):
    if database:
        print("\nList of all students:")
        for name, details in database.items():
            print(f"\nName: {name}")
            for key, value in details.items():
                print(f"{key.capitalize()}: {value}")
    else:
        print("No students in the database.")

def update_student(database):
    name = input("Enter the name of the student to update: ").strip()
    if name in database:
        print(f"\nCurrent details for '{name}':")
        for key, value in database[name].items():
            print(f"{key.capitalize()}: {value}")
        print("\nEnter the updated details. Press Enter to leave unchanged.")
        age = input("Enter new age: ").strip()
        grade = input("Enter new grade: ").strip()
        additional_info = input("Enter new additional details: ").strip()
        if age:
            database[name]["age"] = age
        if grade:
            database[name]["grade"] = grade
        if additional_info:
            database[name]["additional_info"] = additional_info
        print(f"Details for '{name}' have been updated.")
    else:
        print(f"No student found with the name '{name}'.")

def delete_student(database):
    name = input("Enter the name of the student to delete: ").strip()
    if name in database:
        del database[name]
        print(f"Student '{name}' has been deleted.")
    else:
        print(f"No student found with the name '{name}'.")

def main():
    student_database = {}
    while True:
        print("\nStudent Database Menu:")
        print("1. Add Student")
        print("2. View Student")
        print("3. List All Students")
        print("4. Update Student Information")
        print("5. Delete Student")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == "1":
            add_student(student_database)
        elif choice == "2":
            view_student(student_database)
        elif choice == "3":
            list_all_students(student_database)
        elif choice == "4":
            update_student(student_database)
        elif choice == "5":
            delete_student(student_database)
        elif choice == "6":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
