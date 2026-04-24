students = {}

def add_student():
    name = input("Enter student name: ").strip()
    try:
        score = int(input(f"Enter score for {name}: "))
        students[name] = score
        print(f"Added {name} successfully.")
    except ValueError:
        print("Error: Score must be a whole number.")

def view_students():
    if not students:
        print("\n--- No records found ---")
    else:
        print("\n--- Student List ---")
        for name, score in students.items():
            print(f"{name}: {score}")

def update_score():
    name = input("Enter student name to update: ").strip()
    if name in students:
        try:
            new_score = int(input(f"Enter new score for {name}: "))
            students[name] = new_score
            print("Score updated.")
        except ValueError:
            print("Error: Score must be a whole number.")
    else:
        print(f"Error: '{name}' not found in records.")

def delete_student():
    name = input("Enter student name to delete: ").strip()
    if name in students:
        del students[name]
        print(f"Record for {name} deleted.")
    else:
        print(f"Error: '{name}' not found.")

def stats():
    if not students:
        print("No data available to calculate statistics.")
        return
        
    scores = list(students.values())
    avg = sum(scores) / len(scores)
    # Using format specifier :.2f to show only two decimal places
    print(f"\n--- Statistics ---")
    print(f"Average Score: {avg:.2f}")
    print(f"Highest Score: {max(scores)}")
    print(f"Lowest Score:  {min(scores)}")

def main():
    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Score")
        print("4. Delete Student")
        print("5. Statistics")
        print("6. Exit")

        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_score()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            stats()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()