from person import Person

class Student(Person):
    def __init__(self, student_id, name):
        super().__init__(student_id, name)
        self.__courses = []

    def enroll_course(self, course_code):
        if course_code not in self.__courses:
            self.__courses.append(course_code)

    def get_courses(self):
        return self.__courses

    def get_details(self):
        return f"Student ID: {self._person_id}, Name: {self._name}"
