class OnlineClass:
    def __init__(self, course_name, teacher_name):
        self.course_name = course_name
        self.teacher_name = teacher_name

    def show_info(self):
        pass

class SecurityClass(OnlineClass):
    def show_info(self):
        print("Course:", self.course_name)
        print("Teacher:", self.teacher_name)
        print("Subject: Cybersecurity")
        print("Topic: Security+, Ethical Hacking")

class PythonClass(OnlineClass):
    def show_info(self):
        print("Course:",self.course_name)
        print("Teacher:",self.teacher_name)
        print("Subject: Python Programming")
        print("Topics: Python Basics, OOP, Projects")

security = SecurityClass(
    "Security Class",
    "Mg Mg Pyue"
)

python = PythonClass(
    "Python Class",
    "Leon"
)

courses = [security, python]

for course in courses:
    print("\n")
    course.show_info()