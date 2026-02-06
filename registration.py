class Registration:
    def register(self, student, course):
        student.enroll_course(course.code)
