from menu import Menu
from datastore import DataStore
from student import Student
from course import Course
from registration import Registration

class Application:

    @staticmethod
    def run():
        data = DataStore.load_data()
        registration = Registration()

        while True:
            Menu.show_main_menu()
            choice = input("Select option: ")

            if choice == "1":
                sid = input("Student ID: ")
                name = input("Student Name: ")
                data["students"][sid] = {"name": name, "courses": []}
                print("Student added successfully.")

            elif choice == "2":
                code = input("Course Code: ")
                title = input("Course Title: ")
                data["courses"][code] = title
                print("Course added successfully.")

            elif choice == "3":
                sid = input("Student ID: ")
                code = input("Course Code: ")

                if sid in data["students"] and code in data["courses"]:
                    student = Student(sid, data["students"][sid]["name"])
                    for c in data["students"][sid]["courses"]:
                        student.enroll_course(c)

                    course = Course(code, data["courses"][code])
                    registration.register(student, course)

                    data["students"][sid]["courses"] = student.get_courses()
                    print("Student registered successfully.")
                else:
                    print("Invalid student or course.")

            elif choice == "4":
                for sid, info in data["students"].items():
                    print(f"\nID: {sid}, Name: {info['name']}")
                    print("Courses:", ", ".join(info["courses"]) or "None")

            elif choice == "5":
                DataStore.save_data(data)
                print("Exiting...")
                break
