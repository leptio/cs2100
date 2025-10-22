from datetime import datetime
from typing import TypeVar

T = TypeVar('T', bound='Person')  # Generic type that must be a subclass of Person

class Person:
    def __init__(self, name: str, birth_year: int):
        self.name = name
        self.birth_year = birth_year
    
    @classmethod
    def from_birth_date(cls: type[T], name: str, birth_date_str: str) -> T:
        year = datetime.strptime(birth_date_str, "%Y-%m-%d").year
        return cls(name, year)
    
    @classmethod
    def baby(cls: type[T], name: str) -> T:
        return cls(name, datetime.now().year)

person1 = Person('Mini', 2015)
person2 = Person.from_birth_date('Binnie', "2020-03-15")
person3 = Person.baby('Ginnie')