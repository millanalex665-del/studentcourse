class Course:
    def __init__(self, code, title):
        self.code = code
        self.title = title

    def get_details(self):
        return f"{self.code} - {self.title}"
