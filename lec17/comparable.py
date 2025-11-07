#python allows custom <, >, ==, !=, <=, >= by implementing:
#__eq__ (==)
#__ne__ (!=)
#__lt__ (<)
#__le__ (<=)
#__gt__ (>)
#__ge__ (>=)
#usually implement __eq__ and one ordering method (__lt__)

class Course:
    def __init__(self, department:str, course:int):
        self.department = department
        self.course = course

    def __eq__(self, other:object) -> bool:
        if not isinstance(other, Course):
            raise NotImplementedError
        return self.department == other.department and self.course == other.course

course_oakland: Course = Course('cs', 2100)
course_boston: Course = Course('cs', 2100)
print(course_boston == course_oakland)
