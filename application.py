from menu import Menu
from datastore import DataStore
from registration import Registration
from student import Student
from course import Course

class Application:
    def __init__(self):
        self.data = DataStore.load_data()
        self.registration = Registration()

    def run(self):
        while True:
            Menu.show_main_menu()
            choice = input("Select option: ")

            # 1. Add Student
            if choice == "1":
                sid = input("Student ID: ")
                name = input("Student Name: ")
                self.data["students"][sid] = {"name": name, "courses": []}
                DataStore.save_data(self.data) # AUTO-SAVE
                print("Student added and saved.")

            # 2. Add Course
            elif choice == "2":
                code = input("Course Code: ")
                title = input("Course Title: ")
                self.data["courses"][code] = title
                DataStore.save_data(self.data) # AUTO-SAVE
                print("Course added and saved.")

            # 3. Register Student to Course
            elif choice == "3":
                sid = input("Student ID: ")
                code = input("Course Code: ")

                if sid in self.data["students"] and code in self.data["courses"]:
                    # Recreate object from stored data
                    student = Student(sid, self.data["students"][sid]["name"])
                    student.set_courses(self.data["students"][sid]["courses"])
                    
                    course = Course(code, self.data["courses"][code])

                    # Register using your registration logic
                    self.registration.register(student, course)

                    # Update the main data dictionary with the new course list
                    self.data["students"][sid]["courses"] = student.get_courses()
                    
                    # SAVE TO FILE IMMEDIATELY
                    DataStore.save_data(self.data)
                    print(f"Registration successful. Data synced to {DataStore.FILE_NAME}")
                else:
                    print("Error: ID or Course Code not found.")

            # 4. Display
            elif choice == "4":
                if not self.data["students"]:
                    print("No students found.")
                for sid, info in self.data["students"].items():
                    print(f"\nID: {sid} | Name: {info['name']}")
                    print(f"Courses: {', '.join(info['courses']) if info['courses'] else 'None'}")

            # 5. Exit
            elif choice == "5":
                DataStore.save_data(self.data)
                print("System closed safely.")
                break