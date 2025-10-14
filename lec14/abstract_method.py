import math
from abc import ABC, abstractmethod
#abstract is different from override:
#override is optional (option to use parent logic or not override at all)

class Shape(ABC):
    @abstractmethod
    def get_area(self) -> float:
        #to be implemented by subclass
        pass
    @abstractmethod
    def get_perimeter(self) -> float:
        #to be implemented by subclass
        pass

class Rectangle(Shape):
    def __init__(self, length: float, width:float) -> None:
        self.length = length
        self.width = width
    def get_area(self) -> float:
        return self.length*self.width
    def get_perimeter(self) -> float:
        return 2 * (self.width+self.length)

class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self.radius = radius
    def get_area(self) -> float:
        return math.pi*math.pow(self.radius, 2)
    def get_perimeter(self) -> float:
        return 2*math.pi*self.radius

rect = Rectangle(20, 10)
print(rect.get_area())
print(rect.get_perimeter())


circ = Circle(10)
print(circ.get_area())
print(circ.get_perimeter())

#shape = Shape()
#Raises TypeError if uncommented because class is abstract and has abstract methods