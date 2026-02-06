from person import Person

class Student(Person):
    def __init__(self, student_id, name):
        # Call parent constructor
        super().__init__(student_id, name)
        
        # Private list of courses (encapsulation)
        self.__courses = []

    def enroll_course(self, course_code):
        # Prevent duplicate registration
        if course_code not in self.__courses:
            self.__courses.append(course_code)

    def get_courses(self):
        # Controlled access to private data
        return self.__courses

    # Polymorphism: override parent method
    def get_details(self):
        return f"Student ID: {self._person_id}, Name: {self._name}"

