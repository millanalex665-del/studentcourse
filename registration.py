class Registration:
    def register(self, student, course):
        # Register student only if not already enrolled
        if course.code not in student.get_courses():
            student.enroll_course(course.code)
        else:
            print("Student already registered in this course.")

