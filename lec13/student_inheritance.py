from typing import Set
class Student():
    def __init__(self, student_id: str, major: str):
        self.id = student_id
        self.major = major
        self.courses: Set[str] = set()

    def attend_lab(self, course_id: str) -> None:
        if course_id in self.courses:
            print(f'Attending {course_id}\' lab')

    def register_courses(self, courses: Set[str]) -> None:
        self.courses |= courses

class UndergraduateStudent(Student):
    def change_major(self, new_major: str) -> None:
        self.major = new_major

Lee = UndergraduateStudent('12345', 'Computer Science')
Lee.register_courses({'CS101','MATH202'})