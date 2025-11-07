
from collections.abc import Hashable
from typing import Set

class Course(Hashable):
    def __init__(self, department: str, course: int):
        self.department = department
        self.course = course

    def __str__(self) -> str:
        return f'{self.department}{self.course}'

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Course):
            raise NotImplementedError
        else:
            return self.department == other.department and self.course == other.course

    def __hash__(self) -> int:
        return hash(str(self))


course_oakland = Course('CS', 2100)
course_boston = Course('CS', 2100)

courses: Set[Course] = {course_oakland}
courses.add(course_boston)

print(courses)