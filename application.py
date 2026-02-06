from menu import Menu
from datastore import DataStore
from registration import Registration
from student import Student
from course import Course

class Application:
    def __init__(self):
        # Load saved data from JSON file
        self.data = DataStore.load_data()
        
        # Create registration handler
        self.registration = Registration()

    def run(self):
        # Loop keeps the program running until user exits
        while True:
            Menu.show_main_menu()
            choice = input("Select option: ")

            # Add new student
            if choice == "1":
                sid = input("Student ID: ")
                name = input("Student Name: ")
                self.data["students"][sid] = {"name": name, "courses": []}
                print("Student added successfully.")

            # Add new course
            elif choice == "2":
                code = input("Course Code: ")
                title = input("Course Title: ")
                self.data["courses"][code] = title
                print("Course added successfully.")

            # Register student to course
            elif choice == "3":
                sid = input("Student ID: ")
                code = input("Course Code: ")

                # Validate student and course existence
                if sid in self.data["students"] and code in self.data["courses"]:
                    # Create student object
                    student = Student(sid, self.data["students"][sid]["name"])
                    
                    # Restore student courses from stored data
                    student._Student__courses = self.data["students"][sid]["courses"]
                    
                    # Create course object
                    course = Course(code, self.data["courses"][code])

                    # Register student
                    self.registration.register(student, course)

                    # Save updated courses
                    self.data["students"][sid]["courses"] = student.get_courses()
                    print("Student registered successfully.")
                else:
                    print("Invalid student or course.")

            # Display all students
            elif choice == "4":
                for sid, info in self.data["students"].items():
                    print(f"\nID: {sid}, Name: {info['name']}")
                    print("Courses:", ", ".join(info["courses"]) or "None")

            # Exit and save data
            elif choice == "5":
                DataStore.save_data(self.data)
                print("Data saved. Exiting...")
                break

            else:
                print("Invalid option.")
